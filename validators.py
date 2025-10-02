"""
Input validation and data sanitization utilities
"""
import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class CustomerValidator:
    """Validator for customer data"""
    
    # Regex patterns for validation
    PHONE_PATTERN = re.compile(r'^(\+84|84|0)[1-9][0-9]{8,9}$')
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    CUSTOMER_CODE_PATTERN = re.compile(r'^DL[U|T]\d{5}$')
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate Vietnamese phone number"""
        if not phone:
            return False
        return bool(CustomerValidator.PHONE_PATTERN.match(phone.strip()))
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email address"""
        if not email:
            return False
        return bool(CustomerValidator.EMAIL_PATTERN.match(email.strip()))
    
    @staticmethod
    def validate_customer_code(code: str) -> bool:
        """Validate customer code format (DLU00001, DLT00001)"""
        if not code:
            return False
        return bool(CustomerValidator.CUSTOMER_CODE_PATTERN.match(code.strip()))
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """Validate customer name"""
        if not name or not name.strip():
            return False
        # Name should be at least 2 characters and contain only letters, spaces, and Vietnamese characters
        name = name.strip()
        if len(name) < 2:
            return False
        # Allow Vietnamese characters, letters, spaces, and common punctuation
        return bool(re.match(r'^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂÂÊÔƠĐưăâêôơđ\s\.,\-]+$', name))
    
    @staticmethod
    def validate_address(address: str) -> bool:
        """Validate address"""
        if not address or not address.strip():
            return False
        # Address should be at least 5 characters
        return len(address.strip()) >= 5
    
    @staticmethod
    def validate_customer_data(data: Dict) -> Tuple[bool, List[str]]:
        """Validate complete customer data"""
        errors = []
        
        # Required fields
        required_fields = ['name', 'phone', 'email', 'address']
        for field in required_fields:
            if not data.get(field):
                errors.append(f"Field '{field}' is required")
        
        # Validate name
        if data.get('name') and not CustomerValidator.validate_name(data['name']):
            errors.append("Invalid name format")
        
        # Validate phone
        if data.get('phone') and not CustomerValidator.validate_phone(data['phone']):
            errors.append("Invalid phone number format (Vietnamese format required)")
        
        # Validate email
        if data.get('email') and not CustomerValidator.validate_email(data['email']):
            errors.append("Invalid email format")
        
        # Validate address
        if data.get('address') and not CustomerValidator.validate_address(data['address']):
            errors.append("Address must be at least 5 characters long")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def sanitize_customer_data(data: Dict) -> Dict:
        """Sanitize customer data"""
        sanitized = {}
        
        # Sanitize string fields
        string_fields = ['name', 'phone', 'email', 'address', 'code']
        for field in string_fields:
            if field in data and data[field]:
                # Strip whitespace and limit length
                value = str(data[field]).strip()
                if field == 'name':
                    sanitized[field] = value[:100]  # Max 100 characters
                elif field == 'phone':
                    sanitized[field] = value[:15]   # Max 15 characters
                elif field == 'email':
                    sanitized[field] = value[:255].lower()  # Max 255 characters, lowercase
                elif field == 'address':
                    sanitized[field] = value[:500]  # Max 500 characters
                elif field == 'code':
                    sanitized[field] = value.upper()  # Uppercase
            else:
                sanitized[field] = data.get(field, '')
        
        return sanitized

class SearchValidator:
    """Validator for search parameters"""
    
    @staticmethod
    def validate_search_query(query: str) -> bool:
        """Validate search query"""
        if not query:
            return False
        # Query should be at least 1 character and not too long
        return 1 <= len(query.strip()) <= 100
    
    @staticmethod
    def sanitize_search_query(query: str) -> str:
        """Sanitize search query"""
        if not query:
            return ""
        # Remove potentially dangerous characters
        sanitized = re.sub(r'[<>"\']', '', query.strip())
        return sanitized[:100]  # Limit length

class PaginationValidator:
    """Validator for pagination parameters"""
    
    @staticmethod
    def validate_pagination(page: int, per_page: int) -> Tuple[bool, List[str]]:
        """Validate pagination parameters"""
        errors = []
        
        if page < 1:
            errors.append("Page must be greater than 0")
        
        if per_page < 1 or per_page > 100:
            errors.append("Per page must be between 1 and 100")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def sanitize_pagination(page: int, per_page: int) -> Tuple[int, int]:
        """Sanitize pagination parameters"""
        page = max(1, int(page)) if page else 1
        per_page = max(1, min(100, int(per_page))) if per_page else 10
        return page, per_page

def validate_and_sanitize_customer(data: Dict) -> Tuple[Dict, List[str]]:
    """Convenience function to validate and sanitize customer data"""
    # First sanitize
    sanitized_data = CustomerValidator.sanitize_customer_data(data)
    
    # Then validate
    is_valid, errors = CustomerValidator.validate_customer_data(sanitized_data)
    
    return sanitized_data, errors
