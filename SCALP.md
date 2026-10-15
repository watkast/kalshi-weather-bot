# Range-Scalp Bot

*Updated Thu Oct 15 22:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18299 | 15887 | 2412 (28) | 1 | $-5604.25 | -4.9% |
| **+10¢** | 13809 | 11021 | 2788 (40) | 3 | $-5041.73 | -5.8% |
| **+15¢** | 11582 | 8583 | 2999 (59) | 3 | $-4555.32 | -6.3% |
| **+20¢** | 10288 | 7152 | 3136 (78) | 3 | $-3954.78 | -6.1% |
| **+10¢ (15¢ stop)** | 22520 | 22470 | 50 (29) | 0 | $-8718.21 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 22:54 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 10-15 22:54 | +10 stop | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-15 22:54 | +10 stop | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 10-15 22:54 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 10-15 22:54 | +10 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 10-15 22:54 | +5 | XRP | DOWN | 0.71 | 0.80 | 0.63 |
| 10-15 22:54 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 10-15 22:54 | +5 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-15 22:53 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-15 22:53 | +10 stop | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-15 22:52 | +10 stop | SOL | UP | 0.55 | 0.39 | -1.95 |
| 10-15 22:52 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.14 |
| 10-15 22:52 | +10 stop | DOGE | UP | 0.57 | 0.38 | -2.25 |
| 10-15 22:52 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 10-15 22:52 | +15 | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-15 22:52 | +10 | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 10-15 22:52 | +5 | XRP | DOWN | 0.59 | 0.68 | 0.57 |
| 10-15 22:52 | +10 stop | BTC | UP | 0.62 | 0.41 | -2.44 |
| 10-15 22:51 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-15 22:51 | +20 | HYPE | DOWN | 0.67 | 0.91 | 2.22 |
| 10-15 22:51 | +15 | HYPE | DOWN | 0.67 | 0.86 | 1.65 |
| 10-15 22:51 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-15 22:51 | +5 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-15 22:51 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-15 22:51 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-15 22:50 | +10 | ZEC | DOWN | 0.59 | 0.88 | 2.65 |
| 10-15 22:50 | +5 | ZEC | DOWN | 0.59 | 0.68 | 0.57 |
| 10-15 22:50 | +10 stop | DOGE | DOWN | 0.65 | 0.44 | -2.44 |
| 10-15 22:49 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 10-15 22:49 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.49 |
| 10-15 22:49 | +5 | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 10-15 22:49 | +10 stop | SOL | DOWN | 0.59 | 0.40 | -2.24 |
| 10-15 22:49 | +10 stop | ZEC | DOWN | 0.61 | 0.43 | -2.15 |
| 10-15 22:49 | +10 stop | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 10-15 22:49 | +10 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 10-15 22:49 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 10-15 22:49 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-15 22:48 | +10 stop | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-15 22:48 | +10 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-15 22:48 | +5 | SOL | DOWN | 0.57 | 0.63 | 0.25 |
