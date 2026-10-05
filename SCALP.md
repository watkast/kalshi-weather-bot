# Range-Scalp Bot

*Updated Mon Oct 05 08:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3585 | 3074 | 511 (3) | 0 | $-1326.61 | -5.9% |
| **+10¢** | 2767 | 2180 | 587 (4) | 2 | $-1222.05 | -7.0% |
| **+15¢** | 2328 | 1709 | 619 (6) | 2 | $-1090.10 | -7.5% |
| **+20¢** | 2075 | 1430 | 645 (11) | 3 | $-958.14 | -7.4% |
| **+10¢ (15¢ stop)** | 4433 | 4432 | 1 (1) | 0 | $-1701.97 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 08:52 | +10 stop | BNB | DOWN | 0.57 | 0.77 | 1.69 |
| 10-05 08:51 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 08:51 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-05 08:51 | +15 | BTC | DOWN | 0.63 | open |  |
| 10-05 08:51 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 08:51 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-05 08:51 | +10 stop | HYPE | DOWN | 0.67 | 0.85 | 1.51 |
| 10-05 08:51 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-05 08:51 | +15 | HYPE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-05 08:51 | +10 | HYPE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-05 08:51 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-05 08:51 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-05 08:51 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-05 08:51 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-05 08:51 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-05 08:51 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-05 08:51 | +15 | BNB | DOWN | 0.56 | 0.77 | 1.76 |
| 10-05 08:50 | +10 stop | BNB | DOWN | 0.70 | 0.55 | -1.83 |
| 10-05 08:50 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-05 08:50 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 10-05 08:49 | +10 stop | DOGE | DOWN | 0.57 | 0.72 | 1.17 |
| 10-05 08:49 | +20 | DOGE | DOWN | 0.56 | 0.79 | 2.00 |
| 10-05 08:49 | +15 | DOGE | DOWN | 0.56 | 0.72 | 1.27 |
| 10-05 08:49 | +10 | DOGE | DOWN | 0.56 | 0.72 | 1.27 |
| 10-05 08:49 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-05 08:49 | +10 stop | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 10-05 08:49 | +20 | BNB | DOWN | 0.54 | 0.77 | 1.99 |
| 10-05 08:49 | +15 | BNB | DOWN | 0.54 | 0.69 | 1.17 |
| 10-05 08:49 | +10 | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 10-05 08:49 | +5 | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 10-05 08:41 | +10 stop | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-05 08:41 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-05 08:41 | +15 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-05 08:39 | +10 stop | XRP | DOWN | 0.61 | 0.81 | 1.70 |
| 10-05 08:39 | +5 | XRP | DOWN | 0.61 | 0.81 | 1.70 |
| 10-05 08:37 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-05 08:36 | +10 stop | ZEC | UP | 0.57 | 0.35 | -2.54 |
| 10-05 08:36 | +10 | ZEC | UP | 0.57 | 0.84 | 2.42 |
| 10-05 08:36 | +5 | ZEC | UP | 0.56 | 0.84 | 2.52 |
| 10-05 08:36 | +10 stop | XRP | UP | 0.45 | 0.25 | -2.32 |
