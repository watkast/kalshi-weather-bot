# Range-Scalp Bot

*Updated Mon Oct 12 08:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13268 | 11466 | 1802 (25) | 0 | $-4325.62 | -5.2% |
| **+10¢** | 10055 | 7967 | 2088 (37) | 0 | $-4040.51 | -6.4% |
| **+15¢** | 8459 | 6228 | 2231 (55) | 0 | $-3556.36 | -6.7% |
| **+20¢** | 7532 | 5206 | 2326 (70) | 2 | $-3027.19 | -6.4% |
| **+10¢ (15¢ stop)** | 16343 | 16302 | 41 (25) | 0 | $-6405.48 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 08:16 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.83 |
| 10-12 08:16 | +20 | NEAR | DOWN | 0.68 | open |  |
| 10-12 08:16 | +15 | NEAR | DOWN | 0.68 | 0.83 | 1.25 |
| 10-12 08:16 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-12 08:16 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-12 08:16 | +10 stop | HYPE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-12 08:16 | +20 | HYPE | DOWN | 0.54 | 0.79 | 2.16 |
| 10-12 08:16 | +15 | HYPE | DOWN | 0.54 | 0.79 | 2.16 |
| 10-12 08:16 | +10 | HYPE | DOWN | 0.54 | 0.68 | 1.02 |
| 10-12 08:16 | +5 | HYPE | DOWN | 0.54 | 0.60 | 0.21 |
| 10-12 08:15 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-12 08:15 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-12 08:15 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 10-12 08:15 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-12 08:15 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-12 08:02 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 10-12 08:01 | +10 stop | NEAR | UP | 0.47 | 0.29 | -2.17 |
| 10-12 08:01 | +20 | NEAR | UP | 0.48 | no | -4.98 |
| 10-12 08:01 | +15 | NEAR | UP | 0.48 | no | -4.98 |
| 10-12 08:01 | +10 | NEAR | UP | 0.48 | no | -4.98 |
| 10-12 08:01 | +5 | NEAR | UP | 0.48 | 0.54 | 0.24 |
| 10-12 08:01 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 08:01 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.94 |
| 10-12 08:01 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-12 08:01 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 08:01 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-12 08:01 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-12 08:01 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-12 08:01 | +15 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-12 08:01 | +10 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-12 08:01 | +5 | ZEC | DOWN | 0.63 | 0.74 | 0.78 |
| 10-12 08:01 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-12 08:01 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-12 08:01 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 10-12 08:01 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-12 08:01 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-12 07:57 | +10 stop | XRP | DOWN | 0.59 | 0.82 | 2.02 |
| 10-12 07:57 | +10 stop | BNB | DOWN | 0.63 | 0.86 | 2.01 |
| 10-12 07:57 | +15 | BNB | DOWN | 0.63 | 0.86 | 2.01 |
| 10-12 07:57 | +10 stop | XRP | UP | 0.62 | 0.44 | -2.15 |
