import { writable } from 'svelte/store';

export const actors = writable([])
export const map = writable(new Map())
export const dots = writable([])