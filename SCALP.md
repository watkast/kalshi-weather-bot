# Range-Scalp Bot

*Updated Sat Oct 31 22:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42840 | 37353 | 5487 (62) | 0 | $-12101.75 | -4.5% |
| **+10¢** | 31941 | 25593 | 6348 (84) | 0 | $-10876.07 | -5.4% |
| **+15¢** | 26724 | 19881 | 6843 (112) | 0 | $-9955.75 | -5.9% |
| **+20¢** | 23732 | 16560 | 7172 (145) | 1 | $-8826.17 | -5.9% |
| **+10¢ (15¢ stop)** | 52257 | 52174 | 83 (48) | 0 | $-19805.55 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 22:38 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 10-31 22:37 | +10 stop | XRP | DOWN | 0.55 | 0.67 | 0.86 |
| 10-31 22:37 | +10 | XRP | DOWN | 0.55 | 0.67 | 0.86 |
| 10-31 22:37 | +5 | XRP | DOWN | 0.56 | 0.62 | 0.30 |
| 10-31 22:36 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-31 22:36 | +20 | ETH | DOWN | 0.68 | 0.91 | 2.06 |
| 10-31 22:36 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-31 22:36 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-31 22:36 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-31 22:36 | +10 stop | BTC | UP | 0.50 | 0.33 | -2.04 |
| 10-31 22:34 | +5 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 10-31 22:32 | +10 stop | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-31 22:32 | +10 | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-31 22:32 | +5 | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-31 22:32 | +10 stop | BNB | DOWN | 0.57 | 0.81 | 2.11 |
| 10-31 22:32 | +20 | BNB | DOWN | 0.57 | 0.81 | 2.11 |
| 10-31 22:32 | +15 | BNB | DOWN | 0.57 | 0.81 | 2.11 |
| 10-31 22:32 | +10 | BNB | DOWN | 0.57 | 0.81 | 2.09 |
| 10-31 22:32 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-31 22:31 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 22:31 | +20 | HYPE | DOWN | 0.60 | 0.83 | 2.03 |
| 10-31 22:31 | +15 | HYPE | DOWN | 0.60 | 0.83 | 2.03 |
| 10-31 22:31 | +10 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 22:31 | +5 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 22:31 | +10 stop | BTC | DOWN | 0.65 | 0.45 | -2.34 |
| 10-31 22:31 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-31 22:31 | +15 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-31 22:31 | +10 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-31 22:31 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-31 22:31 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-31 22:31 | +20 | XRP | DOWN | 0.66 | 0.92 | 2.34 |
| 10-31 22:31 | +15 | XRP | DOWN | 0.66 | 0.92 | 2.34 |
| 10-31 22:31 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-31 22:31 | +5 | XRP | DOWN | 0.66 | 0.73 | 0.40 |
| 10-31 22:28 | +10 stop | NEAR | UP | 0.68 | 0.53 | -1.84 |
| 10-31 22:26 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-31 22:25 | +10 stop | HYPE | UP | 0.51 | 0.63 | 0.88 |
| 10-31 22:24 | +10 stop | XRP | DOWN | 0.59 | 0.70 | 0.78 |
| 10-31 22:24 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.27 |
| 10-31 22:22 | +5 | XRP | UP | 0.46 | 0.59 | 0.95 |
