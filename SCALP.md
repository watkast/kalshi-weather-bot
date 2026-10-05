# Range-Scalp Bot

*Updated Mon Oct 05 02:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3141 | 2688 | 453 (3) | 2 | $-1196.84 | -6.0% |
| **+10¢** | 2436 | 1923 | 513 (4) | 2 | $-1058.11 | -6.9% |
| **+15¢** | 2050 | 1509 | 541 (5) | 4 | $-935.68 | -7.3% |
| **+20¢** | 1827 | 1265 | 562 (10) | 7 | $-795.55 | -6.9% |
| **+10¢ (15¢ stop)** | 3919 | 3918 | 1 (1) | 2 | $-1552.96 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 02:33 | +10 stop | NEAR | UP | 0.65 | open |  |
| 10-05 02:33 | +5 | NEAR | UP | 0.65 | open |  |
| 10-05 02:32 | +10 stop | DOGE | DOWN | 0.52 | 0.65 | 0.96 |
| 10-05 02:32 | +15 | DOGE | DOWN | 0.52 | open |  |
| 10-05 02:32 | +10 | DOGE | DOWN | 0.52 | 0.65 | 0.96 |
| 10-05 02:32 | +5 | DOGE | DOWN | 0.52 | 0.65 | 0.96 |
| 10-05 02:32 | +5 | NEAR | DOWN | 0.31 | 0.54 | 1.97 |
| 10-05 02:31 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 10-05 02:31 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-05 02:31 | +15 | XRP | DOWN | 0.69 | open |  |
| 10-05 02:31 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-05 02:31 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-05 02:31 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-05 02:31 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-05 02:31 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.20 |
| 10-05 02:31 | +10 | DOGE | DOWN | 0.59 | 0.74 | 1.20 |
| 10-05 02:31 | +5 | DOGE | DOWN | 0.60 | 0.68 | 0.50 |
| 10-05 02:31 | +10 stop | NEAR | DOWN | 0.50 | 0.29 | -2.43 |
| 10-05 02:31 | +20 | NEAR | DOWN | 0.50 | open |  |
| 10-05 02:31 | +15 | NEAR | DOWN | 0.50 | open |  |
| 10-05 02:31 | +10 | NEAR | DOWN | 0.50 | open |  |
| 10-05 02:31 | +5 | NEAR | DOWN | 0.50 | 0.55 | 0.16 |
| 10-05 02:31 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-05 02:31 | +20 | HYPE | DOWN | 0.65 | open |  |
| 10-05 02:31 | +15 | HYPE | DOWN | 0.65 | open |  |
| 10-05 02:31 | +10 | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-05 02:31 | +5 | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-05 02:31 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-05 02:31 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-05 02:31 | +15 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-05 02:31 | +10 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-05 02:31 | +5 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-05 02:31 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-05 02:31 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-05 02:31 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-05 02:31 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-05 02:31 | +5 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-05 02:31 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-05 02:31 | +20 | BTC | DOWN | 0.63 | open |  |
| 10-05 02:31 | +15 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
