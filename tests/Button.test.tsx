import { render, screen } from '@testing-library/react';
import { Button } from './Button';

test('renders button label', () => {
  render(<Button label="Click me" />);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});