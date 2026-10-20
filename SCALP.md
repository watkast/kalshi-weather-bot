# Range-Scalp Bot

*Updated Tue Oct 20 13:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25681 | 22366 | 3315 (31) | 0 | $-7498.55 | -4.6% |
| **+10¢** | 19326 | 15498 | 3828 (46) | 0 | $-6615.60 | -5.4% |
| **+15¢** | 16180 | 12058 | 4122 (70) | 0 | $-5920.33 | -5.8% |
| **+20¢** | 14310 | 9996 | 4314 (88) | 2 | $-5278.20 | -5.9% |
| **+10¢ (15¢ stop)** | 31506 | 31453 | 53 (30) | 0 | $-11610.63 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 13:11 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-20 13:11 | +10 | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-20 13:11 | +5 | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-20 13:11 | +10 stop | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 10-20 13:11 | +5 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 10-20 13:11 | +10 stop | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 13:11 | +20 | XRP | DOWN | 0.64 | 0.87 | 2.05 |
| 10-20 13:11 | +15 | XRP | DOWN | 0.64 | 0.87 | 2.05 |
| 10-20 13:11 | +10 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 13:11 | +5 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 13:11 | +10 stop | DOGE | DOWN | 0.49 | 0.71 | 1.87 |
| 10-20 13:11 | +20 | DOGE | DOWN | 0.49 | 0.71 | 1.87 |
| 10-20 13:11 | +15 | DOGE | DOWN | 0.49 | 0.71 | 1.87 |
| 10-20 13:11 | +10 | DOGE | DOWN | 0.49 | 0.71 | 1.87 |
| 10-20 13:11 | +5 | DOGE | DOWN | 0.49 | 0.56 | 0.34 |
| 10-20 13:11 | +10 stop | ETH | DOWN | 0.51 | 0.62 | 0.75 |
| 10-20 13:11 | +15 | ETH | DOWN | 0.51 | 0.70 | 1.57 |
| 10-20 13:11 | +10 | ETH | DOWN | 0.51 | 0.62 | 0.75 |
| 10-20 13:11 | +5 | ETH | DOWN | 0.50 | 0.62 | 0.85 |
| 10-20 13:10 | +10 stop | SOL | DOWN | 0.58 | 0.40 | -2.15 |
| 10-20 13:10 | +15 | SOL | DOWN | 0.57 | 0.76 | 1.59 |
| 10-20 13:10 | +10 | SOL | DOWN | 0.57 | 0.76 | 1.59 |
| 10-20 13:10 | +5 | SOL | DOWN | 0.57 | 0.62 | 0.15 |
| 10-20 13:07 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-20 13:07 | +20 | ETH | DOWN | 0.64 | open |  |
| 10-20 13:07 | +15 | ETH | DOWN | 0.64 | 0.81 | 1.42 |
| 10-20 13:07 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-20 13:07 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 10-20 13:07 | +10 stop | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-20 13:07 | +20 | XRP | DOWN | 0.68 | 0.88 | 1.76 |
| 10-20 13:07 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-20 13:07 | +10 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-20 13:07 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-20 13:07 | +10 | SOL | DOWN | 0.57 | 0.74 | 1.38 |
| 10-20 13:07 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 10-20 13:05 | +10 stop | HYPE | DOWN | 0.66 | 0.84 | 1.50 |
| 10-20 13:05 | +20 | HYPE | DOWN | 0.66 | 0.87 | 1.82 |
| 10-20 13:05 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.50 |
| 10-20 13:05 | +10 | HYPE | DOWN | 0.67 | 0.84 | 1.40 |
| 10-20 13:05 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.36 |
