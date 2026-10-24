# Range-Scalp Bot

*Updated Sat Oct 24 14:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32110 | 27990 | 4120 (40) | 0 | $-9218.89 | -4.6% |
| **+10¢** | 24034 | 19268 | 4766 (58) | 0 | $-8240.78 | -5.4% |
| **+15¢** | 20122 | 14995 | 5127 (81) | 0 | $-7395.06 | -5.9% |
| **+20¢** | 17827 | 12460 | 5367 (103) | 0 | $-6573.25 | -5.9% |
| **+10¢ (15¢ stop)** | 39458 | 39399 | 59 (32) | 0 | $-15112.82 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 14:23 | +10 stop | BNB | UP | 0.59 | 0.39 | -2.34 |
| 10-24 14:22 | +10 stop | BNB | DOWN | 0.48 | 0.58 | 0.64 |
| 10-24 14:21 | +10 stop | BNB | DOWN | 0.64 | 0.46 | -2.15 |
| 10-24 14:21 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-24 14:21 | +15 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-24 14:21 | +10 | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 14:21 | +5 | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 14:11 | +10 stop | HYPE | UP | 0.50 | 0.63 | 0.95 |
| 10-24 14:11 | +15 | HYPE | UP | 0.51 | no | -5.28 |
| 10-24 14:11 | +10 | HYPE | UP | 0.49 | 0.63 | 1.05 |
| 10-24 14:11 | +5 | HYPE | UP | 0.51 | 0.63 | 0.85 |
| 10-24 14:10 | +10 stop | DOGE | UP | 0.66 | 0.42 | -2.74 |
| 10-24 14:10 | +20 | DOGE | UP | 0.66 | no | -6.76 |
| 10-24 14:10 | +15 | DOGE | UP | 0.66 | no | -6.76 |
| 10-24 14:10 | +10 | DOGE | UP | 0.66 | no | -6.76 |
| 10-24 14:10 | +5 | DOGE | UP | 0.66 | no | -6.76 |
| 10-24 14:10 | +10 stop | BNB | UP | 0.56 | 0.41 | -1.85 |
| 10-24 14:09 | +10 stop | HYPE | DOWN | 0.38 | 0.52 | 1.05 |
| 10-24 14:09 | +10 stop | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 10-24 14:09 | +10 stop | ETH | DOWN | 0.62 | 0.43 | -2.25 |
| 10-24 14:09 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 14:09 | +5 | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 14:08 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.85 |
| 10-24 14:08 | +20 | BNB | UP | 0.64 | no | -6.57 |
| 10-24 14:08 | +15 | BNB | UP | 0.64 | no | -6.57 |
| 10-24 14:08 | +10 | BNB | UP | 0.64 | no | -6.57 |
| 10-24 14:08 | +5 | BNB | UP | 0.64 | no | -6.57 |
| 10-24 14:08 | +10 stop | ZEC | UP | 0.50 | 0.28 | -2.53 |
| 10-24 14:08 | +20 | ZEC | UP | 0.47 | no | -4.88 |
| 10-24 14:08 | +15 | ZEC | UP | 0.47 | no | -4.88 |
| 10-24 14:08 | +10 | ZEC | UP | 0.47 | no | -4.88 |
| 10-24 14:08 | +5 | ZEC | UP | 0.47 | 0.55 | 0.44 |
| 10-24 14:07 | +5 | HYPE | UP | 0.63 | 0.71 | 0.48 |
| 10-24 14:06 | +10 stop | SOL | UP | 0.65 | 0.50 | -1.84 |
| 10-24 14:06 | +15 | SOL | UP | 0.64 | no | -6.57 |
| 10-24 14:06 | +10 | SOL | UP | 0.64 | no | -6.57 |
| 10-24 14:06 | +5 | SOL | UP | 0.64 | no | -6.57 |
| 10-24 14:06 | +10 stop | ETH | UP | 0.67 | 0.51 | -1.94 |
| 10-24 14:06 | +15 | ETH | UP | 0.68 | no | -6.96 |
| 10-24 14:06 | +10 | ETH | UP | 0.68 | no | -6.96 |
