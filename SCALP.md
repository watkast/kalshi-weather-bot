# Range-Scalp Bot

*Updated Sun Nov 08 05:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52071 | 45411 | 6660 (80) | 5 | $-14381.38 | -4.4% |
| **+10¢** | 38867 | 31099 | 7768 (106) | 5 | $-13384.24 | -5.5% |
| **+15¢** | 32548 | 24176 | 8372 (135) | 6 | $-12263.68 | -6.0% |
| **+20¢** | 28954 | 20178 | 8776 (180) | 6 | $-10783.01 | -5.9% |
| **+10¢ (15¢ stop)** | 63386 | 63283 | 103 (61) | 0 | $-23401.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 05:55 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-08 05:55 | +10 stop | BNB | UP | 0.65 | 0.79 | 1.12 |
| 11-08 05:53 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-08 05:53 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-08 05:53 | +10 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-08 05:53 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-08 05:50 | +10 stop | BNB | DOWN | 0.56 | 0.28 | -3.13 |
| 11-08 05:50 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-08 05:50 | +10 stop | HYPE | UP | 0.64 | 0.81 | 1.42 |
| 11-08 05:50 | +20 | HYPE | UP | 0.64 | 0.87 | 2.05 |
| 11-08 05:50 | +15 | HYPE | UP | 0.64 | 0.81 | 1.42 |
| 11-08 05:50 | +10 | HYPE | UP | 0.64 | 0.81 | 1.42 |
| 11-08 05:50 | +5 | HYPE | UP | 0.64 | 0.72 | 0.48 |
| 11-08 05:49 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 11-08 05:49 | +10 stop | BTC | DOWN | 0.65 | 0.24 | -4.39 |
| 11-08 05:49 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-08 05:49 | +10 stop | XRP | DOWN | 0.69 | 0.51 | -2.13 |
| 11-08 05:49 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-08 05:49 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-08 05:49 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-08 05:49 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-08 05:49 | +10 stop | DOGE | UP | 0.62 | 0.74 | 0.89 |
| 11-08 05:48 | +10 stop | ETH | UP | 0.68 | 0.83 | 1.24 |
| 11-08 05:48 | +10 | ETH | UP | 0.67 | 0.83 | 1.34 |
| 11-08 05:48 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-08 05:47 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 11-08 05:47 | +10 stop | NEAR | DOWN | 0.55 | 0.35 | -2.34 |
| 11-08 05:47 | +20 | NEAR | DOWN | 0.55 | open |  |
| 11-08 05:47 | +15 | NEAR | DOWN | 0.55 | open |  |
| 11-08 05:47 | +10 | NEAR | DOWN | 0.55 | open |  |
| 11-08 05:47 | +5 | NEAR | DOWN | 0.55 | open |  |
| 11-08 05:46 | +10 stop | BNB | DOWN | 0.51 | 0.62 | 0.75 |
| 11-08 05:46 | +20 | BNB | DOWN | 0.51 | open |  |
| 11-08 05:46 | +15 | BNB | DOWN | 0.50 | open |  |
| 11-08 05:46 | +10 | BNB | DOWN | 0.50 | 0.62 | 0.85 |
| 11-08 05:46 | +5 | BNB | DOWN | 0.50 | 0.57 | 0.34 |
| 11-08 05:46 | +10 stop | DOGE | DOWN | 0.54 | 0.37 | -2.05 |
| 11-08 05:46 | +20 | DOGE | DOWN | 0.54 | open |  |
| 11-08 05:46 | +15 | DOGE | DOWN | 0.54 | open |  |
| 11-08 05:46 | +10 | DOGE | DOWN | 0.54 | open |  |
