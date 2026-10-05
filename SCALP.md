# Range-Scalp Bot

*Updated Mon Oct 05 02:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3154 | 2701 | 453 (3) | 1 | $-1186.89 | -6.0% |
| **+10¢** | 2446 | 1933 | 513 (4) | 3 | $-1045.59 | -6.8% |
| **+15¢** | 2061 | 1520 | 541 (5) | 3 | $-918.98 | -7.1% |
| **+20¢** | 1831 | 1269 | 562 (10) | 7 | $-788.16 | -6.8% |
| **+10¢ (15¢ stop)** | 3936 | 3935 | 1 (1) | 0 | $-1553.90 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 02:43 | +10 stop | HYPE | DOWN | 0.70 | 0.91 | 1.87 |
| 10-05 02:43 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.87 |
| 10-05 02:43 | +15 | HYPE | DOWN | 0.70 | 0.91 | 1.87 |
| 10-05 02:43 | +10 | HYPE | DOWN | 0.70 | 0.91 | 1.87 |
| 10-05 02:43 | +5 | HYPE | DOWN | 0.70 | 0.91 | 1.87 |
| 10-05 02:39 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-05 02:39 | +10 stop | ZEC | DOWN | 0.64 | 0.25 | -4.25 |
| 10-05 02:39 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-05 02:39 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-05 02:39 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-05 02:39 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-05 02:38 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-05 02:38 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-05 02:38 | +15 | ETH | UP | 0.63 | 0.78 | 1.20 |
| 10-05 02:38 | +10 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-05 02:38 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 10-05 02:38 | +10 stop | SOL | UP | 0.61 | 0.36 | -2.84 |
| 10-05 02:38 | +15 | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-05 02:38 | +10 | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-05 02:38 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 10-05 02:37 | +10 stop | BTC | DOWN | 0.41 | 0.62 | 1.76 |
| 10-05 02:37 | +15 | BTC | DOWN | 0.41 | 0.62 | 1.76 |
| 10-05 02:37 | +10 | BTC | DOWN | 0.41 | 0.62 | 1.76 |
| 10-05 02:37 | +5 | BTC | DOWN | 0.41 | 0.62 | 1.76 |
| 10-05 02:36 | +10 stop | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-05 02:36 | +20 | ZEC | DOWN | 0.55 | 0.75 | 1.73 |
| 10-05 02:36 | +15 | ZEC | DOWN | 0.54 | 0.75 | 1.83 |
| 10-05 02:36 | +10 | ZEC | DOWN | 0.55 | 0.75 | 1.73 |
| 10-05 02:36 | +5 | ZEC | DOWN | 0.54 | 0.64 | 0.70 |
| 10-05 02:36 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 10-05 02:36 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 02:36 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-05 02:36 | +10 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 02:36 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.59 |
| 10-05 02:36 | +10 stop | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 10-05 02:36 | +15 | SOL | DOWN | 0.52 | 0.74 | 1.88 |
| 10-05 02:36 | +10 | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 10-05 02:36 | +5 | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 10-05 02:36 | +10 stop | XRP | UP | 0.44 | 0.60 | 1.25 |
| 10-05 02:36 | +10 stop | ETH | DOWN | 0.57 | 0.76 | 1.59 |
