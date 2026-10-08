# Range-Scalp Bot

*Updated Thu Oct 08 23:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8134 | 7033 | 1101 (13) | 4 | $-2679.23 | -5.2% |
| **+10¢** | 6158 | 4857 | 1301 (25) | 3 | $-2643.26 | -6.8% |
| **+15¢** | 5185 | 3816 | 1369 (37) | 4 | $-2161.57 | -6.6% |
| **+20¢** | 4628 | 3208 | 1420 (45) | 6 | $-1749.99 | -6.0% |
| **+10¢ (15¢ stop)** | 9887 | 9857 | 30 (19) | 3 | $-3659.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 23:10 | +15 | ZEC | UP | 0.41 | 0.59 | 1.46 |
| 10-08 23:10 | +10 stop | ETH | UP | 0.50 | open |  |
| 10-08 23:10 | +10 | ZEC | UP | 0.55 | 0.69 | 1.04 |
| 10-08 23:10 | +10 stop | ZEC | UP | 0.66 | open |  |
| 10-08 23:10 | +10 stop | BTC | DOWN | 0.51 | 0.62 | 0.75 |
| 10-08 23:09 | +10 stop | SOL | UP | 0.70 | open |  |
| 10-08 23:09 | +10 stop | HYPE | DOWN | 0.50 | 0.28 | -2.53 |
| 10-08 23:08 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-08 23:08 | +10 stop | ZEC | DOWN | 0.62 | 0.38 | -2.74 |
| 10-08 23:08 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-08 23:08 | +10 stop | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-08 23:08 | +10 stop | ETH | DOWN | 0.44 | 0.66 | 1.86 |
| 10-08 23:07 | +10 stop | HYPE | DOWN | 0.67 | 0.46 | -2.44 |
| 10-08 23:07 | +10 stop | XRP | UP | 0.55 | 0.72 | 1.37 |
| 10-08 23:07 | +5 | XRP | UP | 0.55 | 0.72 | 1.37 |
| 10-08 23:06 | +10 stop | DOGE | UP | 0.67 | 0.48 | -2.24 |
| 10-08 23:06 | +20 | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 10-08 23:06 | +15 | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 10-08 23:06 | +10 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-08 23:06 | +5 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-08 23:06 | +10 stop | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-08 23:05 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-08 23:05 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-08 23:05 | +10 stop | HYPE | UP | 0.64 | 0.48 | -1.95 |
| 10-08 23:05 | +10 | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 10-08 23:05 | +5 | HYPE | UP | 0.64 | 0.71 | 0.38 |
| 10-08 23:04 | +5 | SOL | UP | 0.71 | 0.79 | 0.53 |
| 10-08 23:04 | +5 | ZEC | DOWN | 0.58 | 0.64 | 0.21 |
| 10-08 23:04 | +5 | ETH | UP | 0.68 | open |  |
| 10-08 23:03 | +10 stop | BTC | UP | 0.68 | 0.53 | -1.84 |
| 10-08 23:02 | +10 stop | SOL | UP | 0.67 | 0.52 | -1.84 |
| 10-08 23:02 | +20 | SOL | UP | 0.67 | open |  |
| 10-08 23:02 | +15 | SOL | UP | 0.67 | open |  |
| 10-08 23:02 | +10 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 10-08 23:02 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
| 10-08 23:02 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-08 23:02 | +10 stop | HYPE | UP | 0.61 | 0.73 | 0.85 |
| 10-08 23:02 | +20 | HYPE | UP | 0.61 | open |  |
| 10-08 23:02 | +15 | HYPE | UP | 0.61 | 0.80 | 1.61 |
| 10-08 23:02 | +10 | HYPE | UP | 0.61 | 0.71 | 0.68 |
