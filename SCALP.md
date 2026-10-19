# Range-Scalp Bot

*Updated Mon Oct 19 10:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23841 | 20730 | 3111 (31) | 0 | $-7107.16 | -4.7% |
| **+10¢** | 17935 | 14349 | 3586 (45) | 1 | $-6340.55 | -5.6% |
| **+15¢** | 15021 | 11159 | 3862 (68) | 1 | $-5738.15 | -6.1% |
| **+20¢** | 13297 | 9258 | 4039 (86) | 1 | $-5102.21 | -6.1% |
| **+10¢ (15¢ stop)** | 29332 | 29281 | 51 (30) | 1 | $-11067.85 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 10:00 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 10-19 10:00 | +20 | DOGE | DOWN | 0.71 | open |  |
| 10-19 10:00 | +15 | DOGE | DOWN | 0.71 | open |  |
| 10-19 10:00 | +10 | DOGE | DOWN | 0.71 | open |  |
| 10-19 10:00 | +5 | DOGE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-19 09:59 | +10 stop | BNB | DOWN | 0.44 | 0.58 | 1.04 |
| 10-19 09:59 | +15 | BNB | DOWN | 0.44 | no | 5.42 |
| 10-19 09:59 | +10 | BNB | DOWN | 0.44 | 0.58 | 1.04 |
| 10-19 09:59 | +5 | BNB | DOWN | 0.44 | 0.58 | 1.04 |
| 10-19 09:56 | +5 | BNB | UP | 0.48 | 0.64 | 1.25 |
| 10-19 09:56 | +10 stop | ZEC | DOWN | 0.53 | 0.75 | 1.88 |
| 10-19 09:56 | +5 | BNB | UP | 0.52 | 0.60 | 0.45 |
| 10-19 09:55 | +10 stop | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-19 09:55 | +10 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-19 09:55 | +5 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-19 09:55 | +5 | BNB | UP | 0.64 | 0.70 | 0.28 |
| 10-19 09:53 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 09:53 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-19 09:53 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-19 09:53 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-19 09:53 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-19 09:53 | +5 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-19 09:53 | +5 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-19 09:52 | +10 stop | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-19 09:52 | +10 stop | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 10-19 09:51 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.05 |
| 10-19 09:51 | +10 stop | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 10-19 09:51 | +10 stop | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-19 09:51 | +15 | BNB | UP | 0.63 | 0.78 | 1.20 |
| 10-19 09:51 | +10 | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-19 09:51 | +5 | BNB | UP | 0.63 | 0.69 | 0.28 |
| 10-19 09:51 | +5 | BTC | DOWN | 0.64 | 0.72 | 0.48 |
| 10-19 09:51 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 10-19 09:50 | +5 | ETH | DOWN | 0.58 | 0.67 | 0.56 |
| 10-19 09:50 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-19 09:50 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 09:50 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 09:50 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 10-19 09:50 | +15 | NEAR | DOWN | 0.61 | 0.77 | 1.30 |
| 10-19 09:50 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
