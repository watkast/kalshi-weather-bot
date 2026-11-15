# Range-Scalp Bot

*Updated Sun Nov 15 17:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60977 | 53193 | 7784 (114) | 0 | $-16522.18 | -4.3% |
| **+10¢** | 45551 | 36432 | 9119 (153) | 0 | $-15531.24 | -5.4% |
| **+15¢** | 38150 | 28315 | 9835 (191) | 0 | $-14204.28 | -5.9% |
| **+20¢** | 34002 | 23687 | 10315 (243) | 1 | $-12476.78 | -5.9% |
| **+10¢ (15¢ stop)** | 74226 | 74074 | 152 (90) | 0 | $-27318.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 17:35 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-15 17:35 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-15 17:35 | +10 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-15 17:35 | +5 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-15 17:34 | +10 stop | ZEC | DOWN | 0.59 | 0.86 | 2.44 |
| 11-15 17:34 | +5 | ZEC | DOWN | 0.59 | 0.86 | 2.44 |
| 11-15 17:34 | +5 | XRP | DOWN | 0.68 | 0.77 | 0.61 |
| 11-15 17:34 | +10 stop | DOGE | DOWN | 0.66 | 0.91 | 2.28 |
| 11-15 17:34 | +10 | DOGE | DOWN | 0.66 | 0.91 | 2.28 |
| 11-15 17:34 | +5 | DOGE | DOWN | 0.66 | 0.91 | 2.28 |
| 11-15 17:33 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 17:33 | +20 | HYPE | DOWN | 0.65 | 0.87 | 1.96 |
| 11-15 17:33 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 17:33 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 17:33 | +5 | HYPE | DOWN | 0.65 | 0.74 | 0.60 |
| 11-15 17:33 | +5 | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-15 17:32 | +5 | ZEC | DOWN | 0.55 | 0.60 | 0.15 |
| 11-15 17:32 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 11-15 17:32 | +5 | SOL | DOWN | 0.57 | 0.63 | 0.25 |
| 11-15 17:31 | +10 stop | ZEC | DOWN | 0.58 | 0.42 | -1.96 |
| 11-15 17:31 | +20 | ZEC | DOWN | 0.57 | 0.86 | 2.63 |
| 11-15 17:31 | +15 | ZEC | DOWN | 0.57 | 0.86 | 2.63 |
| 11-15 17:31 | +10 | ZEC | DOWN | 0.57 | 0.86 | 2.63 |
| 11-15 17:31 | +5 | ZEC | DOWN | 0.57 | 0.64 | 0.35 |
| 11-15 17:31 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-15 17:31 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-15 17:31 | +15 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 17:31 | +10 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 11-15 17:31 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 11-15 17:31 | +10 stop | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-15 17:31 | +20 | DOGE | DOWN | 0.58 | 0.91 | 3.06 |
| 11-15 17:31 | +15 | DOGE | DOWN | 0.58 | 0.91 | 3.06 |
| 11-15 17:31 | +10 | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-15 17:31 | +5 | DOGE | DOWN | 0.58 | 0.65 | 0.36 |
| 11-15 17:31 | +10 stop | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-15 17:31 | +20 | NEAR | DOWN | 0.54 | 0.85 | 2.83 |
| 11-15 17:31 | +15 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 11-15 17:31 | +10 | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-15 17:31 | +5 | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-15 17:31 | +10 stop | SOL | DOWN | 0.57 | 0.71 | 1.07 |
