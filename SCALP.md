# Range-Scalp Bot

*Updated Mon Oct 26 23:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35567 | 31033 | 4534 (43) | 0 | $-10004.46 | -4.5% |
| **+10¢** | 26597 | 21354 | 5243 (65) | 0 | $-8842.31 | -5.3% |
| **+15¢** | 22261 | 16622 | 5639 (89) | 0 | $-7917.44 | -5.7% |
| **+20¢** | 19739 | 13829 | 5910 (112) | 0 | $-6980.53 | -5.6% |
| **+10¢ (15¢ stop)** | 43616 | 43554 | 62 (33) | 0 | $-16629.52 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 23:01 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-26 23:01 | +20 | DOGE | DOWN | 0.65 | 0.93 | 2.58 |
| 10-26 23:01 | +15 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-26 23:01 | +10 | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-26 23:01 | +5 | DOGE | DOWN | 0.65 | 0.79 | 1.12 |
| 10-26 23:01 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-26 23:01 | +20 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 10-26 23:01 | +15 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 10-26 23:01 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-26 23:01 | +5 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-26 23:00 | +10 stop | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 10-26 23:00 | +20 | BNB | DOWN | 0.61 | 0.89 | 2.56 |
| 10-26 23:00 | +15 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 10-26 23:00 | +10 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 10-26 23:00 | +5 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 10-26 23:00 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-26 23:00 | +20 | BTC | DOWN | 0.65 | 0.88 | 2.06 |
| 10-26 23:00 | +15 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-26 23:00 | +10 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 10-26 23:00 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-26 23:00 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.90 |
| 10-26 23:00 | +20 | SOL | DOWN | 0.59 | 0.87 | 2.57 |
| 10-26 23:00 | +15 | SOL | DOWN | 0.59 | 0.74 | 1.21 |
| 10-26 23:00 | +10 | SOL | DOWN | 0.59 | 0.71 | 0.90 |
| 10-26 23:00 | +5 | SOL | DOWN | 0.56 | 0.64 | 0.45 |
| 10-26 23:00 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-26 23:00 | +20 | HYPE | DOWN | 0.69 | 0.90 | 1.88 |
| 10-26 23:00 | +15 | HYPE | DOWN | 0.68 | 0.85 | 1.41 |
| 10-26 23:00 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 10-26 23:00 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.26 |
| 10-26 23:00 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-26 23:00 | +20 | ZEC | DOWN | 0.68 | 0.93 | 2.32 |
| 10-26 23:00 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 10-26 23:00 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-26 23:00 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 10-26 22:58 | +10 stop | BTC | UP | 0.62 | 0.03 | -6.07 |
| 10-26 22:57 | +10 stop | BTC | UP | 0.70 | 0.52 | -2.09 |
| 10-26 22:55 | +5 | BTC | DOWN | 0.68 | 0.96 | 2.65 |
| 10-26 22:54 | +10 stop | HYPE | DOWN | 0.52 | 0.66 | 1.06 |
| 10-26 22:53 | +10 stop | BTC | DOWN | 0.63 | 0.47 | -1.95 |
