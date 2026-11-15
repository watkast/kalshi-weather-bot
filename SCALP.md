# Range-Scalp Bot

*Updated Sun Nov 15 21:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61243 | 53441 | 7802 (114) | 0 | $-16478.60 | -4.3% |
| **+10¢** | 45737 | 36595 | 9142 (153) | 0 | $-15476.42 | -5.4% |
| **+15¢** | 38312 | 28454 | 9858 (191) | 0 | $-14107.81 | -5.9% |
| **+20¢** | 34150 | 23809 | 10341 (243) | 0 | $-12373.28 | -5.8% |
| **+10¢ (15¢ stop)** | 74518 | 74366 | 152 (90) | 0 | $-27425.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 21:18 | +20 | HYPE | DOWN | 0.71 | 1.00 | 2.75 |
| 11-15 21:18 | +15 | HYPE | DOWN | 0.71 | 1.00 | 2.75 |
| 11-15 21:18 | +10 | HYPE | DOWN | 0.71 | 1.00 | 2.75 |
| 11-15 21:18 | +5 | HYPE | DOWN | 0.71 | 1.00 | 2.75 |
| 11-15 21:16 | +10 stop | SOL | DOWN | 0.57 | 1.00 | 4.12 |
| 11-15 21:16 | +20 | SOL | DOWN | 0.54 | 1.00 | 4.42 |
| 11-15 21:16 | +15 | SOL | DOWN | 0.54 | 1.00 | 4.42 |
| 11-15 21:16 | +10 | SOL | DOWN | 0.57 | 1.00 | 4.12 |
| 11-15 21:16 | +5 | SOL | DOWN | 0.63 | 1.00 | 3.53 |
| 11-15 21:16 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-15 21:16 | +20 | ZEC | DOWN | 0.65 | 1.00 | 3.34 |
| 11-15 21:16 | +15 | ZEC | DOWN | 0.64 | 1.00 | 3.43 |
| 11-15 21:16 | +10 | ZEC | DOWN | 0.63 | 0.76 | 1.02 |
| 11-15 21:16 | +5 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-15 21:16 | +10 stop | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 11-15 21:16 | +20 | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 11-15 21:16 | +15 | DOGE | DOWN | 0.59 | 0.78 | 1.61 |
| 11-15 21:16 | +10 | DOGE | DOWN | 0.59 | 0.78 | 1.61 |
| 11-15 21:16 | +5 | DOGE | DOWN | 0.59 | 0.78 | 1.61 |
| 11-15 21:16 | +10 stop | NEAR | DOWN | 0.59 | 0.84 | 2.20 |
| 11-15 21:16 | +20 | NEAR | DOWN | 0.59 | 0.84 | 2.20 |
| 11-15 21:16 | +15 | NEAR | DOWN | 0.59 | 0.84 | 2.20 |
| 11-15 21:16 | +10 | NEAR | DOWN | 0.59 | 0.84 | 2.20 |
| 11-15 21:16 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.24 |
| 11-15 21:11 | +10 stop | NEAR | UP | 0.49 | 0.14 | -3.77 |
| 11-15 21:08 | +10 stop | SOL | UP | 0.68 | 0.50 | -2.14 |
| 11-15 21:08 | +10 | SOL | UP | 0.68 | 0.81 | 1.03 |
| 11-15 21:08 | +5 | SOL | UP | 0.68 | 0.76 | 0.51 |
| 11-15 21:08 | +10 stop | NEAR | UP | 0.55 | 0.40 | -1.85 |
| 11-15 21:08 | +20 | NEAR | UP | 0.55 | no | -5.68 |
| 11-15 21:08 | +15 | NEAR | UP | 0.55 | no | -5.68 |
| 11-15 21:08 | +10 | NEAR | UP | 0.55 | no | -5.68 |
| 11-15 21:08 | +5 | NEAR | UP | 0.55 | no | -5.68 |
| 11-15 21:08 | +10 stop | HYPE | DOWN | 0.55 | 0.36 | -2.25 |
| 11-15 21:07 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-15 21:07 | +5 | ZEC | DOWN | 0.60 | 0.69 | 0.58 |
| 11-15 21:06 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-15 21:06 | +10 stop | SOL | UP | 0.53 | 0.29 | -2.73 |
| 11-15 21:06 | +5 | SOL | UP | 0.53 | 0.60 | 0.35 |
| 11-15 21:06 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
