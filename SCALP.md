# Range-Scalp Bot

*Updated Fri Nov 13 08:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58029 | 50628 | 7401 (102) | 2 | $-15702.72 | -4.3% |
| **+10¢** | 43353 | 34703 | 8650 (134) | 2 | $-14663.15 | -5.4% |
| **+15¢** | 36347 | 27035 | 9312 (168) | 2 | $-13212.03 | -5.8% |
| **+20¢** | 32383 | 22607 | 9776 (219) | 3 | $-11591.37 | -5.7% |
| **+10¢ (15¢ stop)** | 70707 | 70578 | 129 (79) | 2 | $-26007.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 08:51 | +5 | BTC | UP | 0.66 | open |  |
| 11-13 08:51 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 11-13 08:51 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-13 08:51 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-13 08:51 | +10 | ZEC | DOWN | 0.65 | open |  |
| 11-13 08:51 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-13 08:50 | +10 stop | BTC | UP | 0.67 | open |  |
| 11-13 08:50 | +10 | BTC | UP | 0.67 | open |  |
| 11-13 08:50 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 11-13 08:46 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-13 08:46 | +20 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 11-13 08:46 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 11-13 08:46 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-13 08:46 | +5 | HYPE | UP | 0.65 | 0.71 | 0.29 |
| 11-13 08:46 | +10 stop | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 11-13 08:46 | +20 | ZEC | UP | 0.56 | 0.76 | 1.69 |
| 11-13 08:46 | +15 | ZEC | UP | 0.56 | 0.71 | 1.17 |
| 11-13 08:46 | +10 | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 11-13 08:46 | +5 | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 11-13 08:46 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-13 08:46 | +20 | BTC | UP | 0.69 | open |  |
| 11-13 08:46 | +15 | BTC | UP | 0.69 | open |  |
| 11-13 08:46 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 11-13 08:46 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 11-13 08:46 | +10 stop | BNB | UP | 0.67 | 0.78 | 0.81 |
| 11-13 08:46 | +20 | BNB | UP | 0.67 | open |  |
| 11-13 08:46 | +15 | BNB | UP | 0.67 | 0.82 | 1.23 |
| 11-13 08:46 | +10 | BNB | UP | 0.67 | 0.78 | 0.81 |
| 11-13 08:46 | +5 | BNB | UP | 0.67 | 0.73 | 0.30 |
| 11-13 08:46 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-13 08:46 | +20 | ETH | UP | 0.66 | 0.86 | 1.75 |
| 11-13 08:46 | +15 | ETH | UP | 0.66 | 0.81 | 1.23 |
| 11-13 08:46 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-13 08:46 | +5 | ETH | UP | 0.66 | 0.74 | 0.50 |
| 11-13 08:40 | +5 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 11-13 08:40 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 11-13 08:40 | +10 stop | ZEC | DOWN | 0.56 | 0.30 | -2.93 |
| 11-13 08:39 | +5 | ETH | UP | 0.62 | 0.71 | 0.58 |
| 11-13 08:38 | +10 stop | SOL | UP | 0.59 | 0.84 | 2.23 |
| 11-13 08:38 | +20 | SOL | UP | 0.59 | 0.84 | 2.23 |
