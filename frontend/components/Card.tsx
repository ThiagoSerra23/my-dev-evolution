import React from 'react';

export const Card = ({ children }: { children: React.ReactNode }) => {
    return <div className="card shadow-md p-4">{children}</div>;
};