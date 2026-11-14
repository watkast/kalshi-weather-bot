# Range-Scalp Bot

*Updated Sat Nov 14 00:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58750 | 51261 | 7489 (106) | 2 | $-15860.55 | -4.3% |
| **+10¢** | 43891 | 35133 | 8758 (139) | 2 | $-14836.27 | -5.4% |
| **+15¢** | 36785 | 27351 | 9434 (174) | 3 | $-13413.86 | -5.8% |
| **+20¢** | 32770 | 22866 | 9904 (225) | 3 | $-11802.93 | -5.7% |
| **+10¢ (15¢ stop)** | 71530 | 71392 | 138 (82) | 1 | $-26341.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 00:24 | +10 stop | NEAR | DOWN | 0.62 | open |  |
| 11-14 00:24 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-14 00:24 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-14 00:24 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-14 00:22 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 11-14 00:22 | +15 | BTC | UP | 0.66 | 0.81 | 1.23 |
| 11-14 00:22 | +10 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 11-14 00:22 | +10 stop | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-14 00:22 | +10 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-14 00:22 | +5 | XRP | UP | 0.61 | 0.68 | 0.37 |
| 11-14 00:21 | +15 | NEAR | DOWN | 0.54 | 0.76 | 1.89 |
| 11-14 00:21 | +5 | NEAR | DOWN | 0.54 | 0.64 | 0.65 |
| 11-14 00:20 | +10 stop | BTC | UP | 0.62 | 0.72 | 0.68 |
| 11-14 00:20 | +10 | BTC | UP | 0.62 | 0.72 | 0.68 |
| 11-14 00:19 | +5 | ETH | UP | 0.65 | 0.73 | 0.50 |
| 11-14 00:19 | +10 stop | BNB | UP | 0.59 | 0.69 | 0.69 |
| 11-14 00:19 | +10 stop | DOGE | UP | 0.61 | 0.75 | 1.09 |
| 11-14 00:19 | +5 | NEAR | DOWN | 0.54 | 0.63 | 0.55 |
| 11-14 00:19 | +10 stop | NEAR | DOWN | 0.60 | 0.40 | -2.34 |
| 11-14 00:19 | +10 | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 11-14 00:19 | +5 | NEAR | DOWN | 0.53 | 0.60 | 0.35 |
| 11-14 00:18 | +10 stop | BTC | UP | 0.49 | 0.64 | 1.15 |
| 11-14 00:18 | +10 | BTC | UP | 0.49 | 0.64 | 1.15 |
| 11-14 00:18 | +10 stop | ETH | UP | 0.53 | 0.64 | 0.75 |
| 11-14 00:18 | +20 | ETH | UP | 0.53 | 0.73 | 1.68 |
| 11-14 00:18 | +15 | ETH | UP | 0.53 | 0.73 | 1.68 |
| 11-14 00:18 | +10 | ETH | UP | 0.53 | 0.64 | 0.75 |
| 11-14 00:18 | +5 | ETH | UP | 0.53 | 0.60 | 0.35 |
| 11-14 00:18 | +5 | NEAR | UP | 0.50 | 0.62 | 0.85 |
| 11-14 00:18 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-14 00:18 | +10 stop | DOGE | UP | 0.70 | 0.52 | -2.13 |
| 11-14 00:18 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 11-14 00:17 | +10 stop | XRP | UP | 0.65 | 0.78 | 1.01 |
| 11-14 00:17 | +10 | XRP | UP | 0.66 | 0.78 | 0.93 |
| 11-14 00:17 | +5 | XRP | UP | 0.66 | 0.72 | 0.31 |
| 11-14 00:17 | +10 stop | NEAR | DOWN | 0.46 | 0.60 | 1.05 |
| 11-14 00:17 | +15 | NEAR | DOWN | 0.46 | 0.63 | 1.35 |
| 11-14 00:17 | +10 | NEAR | DOWN | 0.46 | 0.60 | 1.05 |
| 11-14 00:17 | +5 | NEAR | DOWN | 0.46 | 0.54 | 0.44 |
| 11-14 00:17 | +10 stop | BNB | UP | 0.68 | 0.45 | -2.64 |
