# Range-Scalp Bot

*Updated Fri Oct 23 20:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30894 | 26924 | 3970 (39) | 3 | $-8923.87 | -4.6% |
| **+10¢** | 23106 | 18518 | 4588 (57) | 5 | $-7938.04 | -5.5% |
| **+15¢** | 19328 | 14390 | 4938 (80) | 5 | $-7171.40 | -5.9% |
| **+20¢** | 17122 | 11953 | 5169 (103) | 5 | $-6388.38 | -5.9% |
| **+10¢ (15¢ stop)** | 37913 | 37854 | 59 (32) | 0 | $-14464.43 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 20:11 | +10 stop | ZEC | DOWN | 0.59 | 0.38 | -2.44 |
| 10-23 20:10 | +10 stop | ZEC | UP | 0.58 | 0.40 | -2.15 |
| 10-23 20:09 | +10 stop | SOL | UP | 0.64 | 0.78 | 1.10 |
| 10-23 20:09 | +5 | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-23 20:09 | +5 | SOL | UP | 0.70 | 0.78 | 0.52 |
| 10-23 20:09 | +10 stop | ZEC | UP | 0.56 | 0.67 | 0.79 |
| 10-23 20:09 | +5 | ZEC | UP | 0.55 | 0.65 | 0.66 |
| 10-23 20:08 | +10 stop | ETH | UP | 0.67 | 0.82 | 1.23 |
| 10-23 20:08 | +10 | ETH | UP | 0.67 | 0.82 | 1.23 |
| 10-23 20:08 | +5 | SOL | DOWN | 0.54 | 0.62 | 0.45 |
| 10-23 20:08 | +5 | ETH | UP | 0.61 | 0.67 | 0.27 |
| 10-23 20:08 | +10 stop | HYPE | UP | 0.63 | 0.79 | 1.27 |
| 10-23 20:08 | +10 stop | SOL | DOWN | 0.56 | 0.35 | -2.44 |
| 10-23 20:08 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-23 20:08 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-23 20:08 | +10 | SOL | DOWN | 0.57 | open |  |
| 10-23 20:08 | +5 | SOL | DOWN | 0.57 | 0.64 | 0.35 |
| 10-23 20:08 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 10-23 20:07 | +10 stop | ZEC | DOWN | 0.59 | 0.32 | -3.03 |
| 10-23 20:07 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-23 20:07 | +15 | ZEC | DOWN | 0.58 | open |  |
| 10-23 20:07 | +10 | ZEC | DOWN | 0.58 | open |  |
| 10-23 20:07 | +5 | ZEC | DOWN | 0.58 | 0.67 | 0.56 |
| 10-23 20:07 | +10 stop | BNB | UP | 0.64 | 0.80 | 1.31 |
| 10-23 20:07 | +10 stop | HYPE | DOWN | 0.60 | 0.45 | -1.85 |
| 10-23 20:07 | +10 | HYPE | DOWN | 0.60 | open |  |
| 10-23 20:07 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-23 20:07 | +5 | XRP | UP | 0.58 | 0.67 | 0.56 |
| 10-23 20:07 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 10-23 20:06 | +10 stop | HYPE | DOWN | 0.50 | 0.60 | 0.65 |
| 10-23 20:06 | +20 | HYPE | DOWN | 0.50 | open |  |
| 10-23 20:06 | +15 | HYPE | DOWN | 0.50 | open |  |
| 10-23 20:06 | +10 | HYPE | DOWN | 0.50 | 0.60 | 0.65 |
| 10-23 20:06 | +5 | HYPE | DOWN | 0.50 | 0.60 | 0.65 |
| 10-23 20:06 | +5 | DOGE | UP | 0.59 | 0.67 | 0.47 |
| 10-23 20:06 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-23 20:05 | +10 stop | NEAR | DOWN | 0.55 | 0.33 | -2.58 |
| 10-23 20:05 | +10 stop | BNB | UP | 0.62 | 0.75 | 1.00 |
| 10-23 20:05 | +5 | NEAR | DOWN | 0.60 | open |  |
| 10-23 20:05 | +10 stop | DOGE | UP | 0.58 | 0.79 | 1.80 |
