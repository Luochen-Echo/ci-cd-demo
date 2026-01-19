import { describe, it, expect, vi } from 'vitest'

describe('Simple Tests', () => {
  it('should add numbers correctly', () => {
    expect(2 + 2).toBe(4)
  })

  it('should check string length', () => {
    const str = 'hello'
    expect(str.length).toBe(5)
  })

  it('should verify array operations', () => {
    const arr = [1, 2, 3]
    expect(arr).toContain(2)
    expect(arr.length).toBe(3)
  })
})
