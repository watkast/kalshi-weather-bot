# Range-Scalp Bot

*Updated Tue Nov 03 22:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46390 | 40392 | 5998 (72) | 3 | $-13361.48 | -4.6% |
| **+10¢** | 34634 | 27685 | 6949 (96) | 3 | $-12210.48 | -5.6% |
| **+15¢** | 28994 | 21522 | 7472 (124) | 3 | $-11144.31 | -6.1% |
| **+20¢** | 25759 | 17928 | 7831 (164) | 3 | $-9851.98 | -6.1% |
| **+10¢ (15¢ stop)** | 56584 | 56491 | 93 (56) | 2 | $-21211.21 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 22:06 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 11-03 22:05 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 11-03 22:04 | +10 stop | ZEC | DOWN | 0.71 | 0.84 | 1.05 |
| 11-03 22:04 | +10 stop | BNB | UP | 0.39 | 0.69 | 2.68 |
| 11-03 22:03 | +5 | BNB | UP | 0.69 | open |  |
| 11-03 22:02 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 11-03 22:02 | +20 | ETH | UP | 0.58 | open |  |
| 11-03 22:02 | +15 | ETH | UP | 0.58 | open |  |
| 11-03 22:02 | +10 | ETH | UP | 0.58 | open |  |
| 11-03 22:02 | +5 | ETH | UP | 0.58 | open |  |
| 11-03 22:02 | +10 stop | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-03 22:02 | +20 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-03 22:02 | +15 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-03 22:02 | +10 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-03 22:02 | +5 | SOL | DOWN | 0.56 | 0.63 | 0.35 |
| 11-03 22:02 | +10 stop | ZEC | UP | 0.68 | 0.40 | -3.13 |
| 11-03 22:02 | +20 | ZEC | UP | 0.67 | open |  |
| 11-03 22:02 | +15 | ZEC | UP | 0.65 | open |  |
| 11-03 22:02 | +10 | ZEC | UP | 0.65 | open |  |
| 11-03 22:02 | +5 | ZEC | UP | 0.65 | open |  |
| 11-03 22:01 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-03 22:01 | +20 | BTC | DOWN | 0.58 | 0.82 | 2.11 |
| 11-03 22:01 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-03 22:01 | +10 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-03 22:01 | +5 | BTC | DOWN | 0.59 | 0.68 | 0.57 |
| 11-03 22:01 | +10 | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-03 22:01 | +10 stop | XRP | DOWN | 0.60 | 0.72 | 0.91 |
| 11-03 22:01 | +20 | XRP | DOWN | 0.59 | 0.82 | 1.97 |
| 11-03 22:01 | +15 | XRP | DOWN | 0.59 | 0.75 | 1.24 |
| 11-03 22:01 | +10 | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 22:01 | +5 | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 22:01 | +10 stop | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 11-03 22:01 | +20 | HYPE | DOWN | 0.59 | 0.83 | 2.13 |
| 11-03 22:01 | +15 | HYPE | DOWN | 0.59 | 0.78 | 1.58 |
| 11-03 22:01 | +10 | HYPE | DOWN | 0.59 | 0.74 | 1.17 |
| 11-03 22:01 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.37 |
| 11-03 22:01 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-03 22:01 | +20 | DOGE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-03 22:01 | +15 | DOGE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-03 22:01 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.33 |
