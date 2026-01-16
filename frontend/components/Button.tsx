import React from 'react';

type ButtonProps = {
    label: string;
    onClick: () => void;
    variant?: 'primary' | 'secondary';
};

export const Button = ({ label, onClick, variant = 'primary' }: ButtonProps) => {
    const styles = variant === 'primary'
        ? { backgroundColor: 'blue', color: 'white' }
        : { backgroundColor: 'gray', color: 'black' };

    return (
        <button onClick={onClick} style={{ padding: '10px 20px', ...styles }}>
            {label}
        </button>
    );
};
