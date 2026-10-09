# Range-Scalp Bot

*Updated Fri Oct 09 07:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8744 | 7564 | 1180 (13) | 4 | $-2862.33 | -5.2% |
| **+10¢** | 6624 | 5234 | 1390 (25) | 4 | $-2780.90 | -6.7% |
| **+15¢** | 5586 | 4123 | 1463 (37) | 4 | $-2257.08 | -6.4% |
| **+20¢** | 4973 | 3455 | 1518 (45) | 5 | $-1854.60 | -5.9% |
| **+10¢ (15¢ stop)** | 10665 | 10635 | 30 (19) | 2 | $-3953.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 07:41 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 10-09 07:41 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-09 07:41 | +5 | DOGE | DOWN | 0.59 | open |  |
| 10-09 07:41 | +10 stop | BTC | UP | 0.65 | open |  |
| 10-09 07:41 | +20 | BTC | UP | 0.65 | open |  |
| 10-09 07:41 | +15 | BTC | UP | 0.65 | open |  |
| 10-09 07:41 | +10 | BTC | UP | 0.65 | open |  |
| 10-09 07:41 | +5 | BTC | UP | 0.65 | open |  |
| 10-09 07:39 | +10 stop | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 10-09 07:39 | +20 | DOGE | UP | 0.48 | open |  |
| 10-09 07:39 | +15 | DOGE | UP | 0.48 | open |  |
| 10-09 07:39 | +10 | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 10-09 07:39 | +5 | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 10-09 07:39 | +10 stop | SOL | UP | 0.65 | 0.79 | 1.12 |
| 10-09 07:38 | +10 stop | SOL | UP | 0.63 | 0.45 | -2.15 |
| 10-09 07:36 | +10 stop | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 10-09 07:36 | +10 stop | ZEC | UP | 0.59 | 0.78 | 1.60 |
| 10-09 07:36 | +10 | ZEC | UP | 0.59 | 0.78 | 1.60 |
| 10-09 07:36 | +5 | ZEC | UP | 0.59 | 0.78 | 1.60 |
| 10-09 07:35 | +10 stop | NEAR | UP | 0.58 | 0.41 | -2.05 |
| 10-09 07:35 | +10 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-09 07:35 | +5 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-09 07:35 | +10 stop | ETH | UP | 0.68 | 0.80 | 0.92 |
| 10-09 07:35 | +20 | ETH | UP | 0.68 | open |  |
| 10-09 07:35 | +15 | ETH | UP | 0.68 | 0.83 | 1.24 |
| 10-09 07:35 | +10 | ETH | UP | 0.68 | 0.80 | 0.92 |
| 10-09 07:35 | +5 | ETH | UP | 0.68 | 0.76 | 0.51 |
| 10-09 07:35 | +10 stop | NEAR | UP | 0.53 | 0.66 | 0.96 |
| 10-09 07:35 | +20 | NEAR | UP | 0.53 | 0.78 | 2.19 |
| 10-09 07:35 | +15 | NEAR | UP | 0.53 | 0.68 | 1.16 |
| 10-09 07:35 | +10 | NEAR | UP | 0.55 | 0.66 | 0.78 |
| 10-09 07:35 | +5 | NEAR | UP | 0.55 | 0.66 | 0.76 |
| 10-09 07:33 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 10-09 07:32 | +10 stop | NEAR | UP | 0.54 | 0.71 | 1.37 |
| 10-09 07:32 | +20 | NEAR | UP | 0.54 | 0.79 | 2.20 |
| 10-09 07:32 | +15 | NEAR | UP | 0.54 | 0.71 | 1.37 |
| 10-09 07:32 | +10 | NEAR | UP | 0.54 | 0.71 | 1.37 |
| 10-09 07:32 | +5 | NEAR | UP | 0.54 | 0.60 | 0.25 |
| 10-09 07:32 | +10 stop | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-09 07:32 | +20 | ZEC | UP | 0.64 | 0.84 | 1.73 |
