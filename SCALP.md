# Range-Scalp Bot

*Updated Fri Nov 13 11:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58197 | 50783 | 7414 (102) | 2 | $-15692.05 | -4.3% |
| **+10¢** | 43481 | 34811 | 8670 (134) | 2 | $-14665.97 | -5.4% |
| **+15¢** | 36452 | 27117 | 9335 (168) | 2 | $-13228.05 | -5.8% |
| **+20¢** | 32478 | 22677 | 9801 (219) | 2 | $-11603.53 | -5.7% |
| **+10¢ (15¢ stop)** | 70913 | 70784 | 129 (79) | 0 | $-26082.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 11:10 | +10 stop | SOL | UP | 0.62 | 0.39 | -2.64 |
| 11-13 11:10 | +20 | SOL | UP | 0.62 | open |  |
| 11-13 11:10 | +15 | SOL | UP | 0.63 | open |  |
| 11-13 11:10 | +10 | SOL | UP | 0.63 | open |  |
| 11-13 11:10 | +5 | SOL | UP | 0.63 | open |  |
| 11-13 11:10 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-13 11:10 | +10 stop | BNB | UP | 0.60 | 0.42 | -2.15 |
| 11-13 11:09 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-13 11:07 | +10 stop | BNB | UP | 0.65 | 0.50 | -1.84 |
| 11-13 11:07 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-13 11:07 | +15 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-13 11:07 | +10 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-13 11:07 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-13 11:07 | +10 stop | BTC | UP | 0.63 | 0.41 | -2.54 |
| 11-13 11:06 | +10 stop | BNB | DOWN | 0.62 | 0.42 | -2.35 |
| 11-13 11:06 | +10 stop | BTC | DOWN | 0.70 | 0.52 | -2.13 |
| 11-13 11:04 | +10 stop | ETH | UP | 0.61 | 0.76 | 1.20 |
| 11-13 11:04 | +10 stop | SOL | UP | 0.65 | 0.50 | -1.84 |
| 11-13 11:04 | +10 | SOL | UP | 0.65 | 0.78 | 1.01 |
| 11-13 11:04 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 11-13 11:04 | +10 stop | BNB | UP | 0.68 | 0.42 | -2.94 |
| 11-13 11:04 | +10 stop | HYPE | UP | 0.59 | 0.73 | 1.09 |
| 11-13 11:03 | +10 stop | BTC | UP | 0.62 | 0.46 | -1.95 |
| 11-13 11:03 | +10 stop | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 11-13 11:03 | +10 stop | DOGE | UP | 0.53 | 0.36 | -2.05 |
| 11-13 11:03 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.99 |
| 11-13 11:02 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
| 11-13 11:02 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.81 |
| 11-13 11:02 | +20 | SOL | UP | 0.66 | 0.86 | 1.75 |
| 11-13 11:02 | +15 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-13 11:02 | +10 | SOL | UP | 0.66 | 0.77 | 0.81 |
| 11-13 11:02 | +5 | SOL | UP | 0.65 | 0.72 | 0.39 |
| 11-13 11:01 | +5 | ZEC | UP | 0.68 | 0.75 | 0.40 |
| 11-13 11:00 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.04 |
| 11-13 11:00 | +20 | DOGE | DOWN | 0.67 | 0.88 | 1.86 |
| 11-13 11:00 | +15 | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-13 11:00 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-13 11:00 | +5 | DOGE | DOWN | 0.69 | 0.78 | 0.62 |
| 11-13 11:00 | +10 stop | XRP | DOWN | 0.64 | 0.40 | -2.74 |
| 11-13 11:00 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
