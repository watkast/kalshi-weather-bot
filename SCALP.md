# Range-Scalp Bot

*Updated Sat Oct 31 22:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42802 | 37317 | 5485 (62) | 1 | $-12116.24 | -4.5% |
| **+10¢** | 31916 | 25573 | 6343 (84) | 2 | $-10874.75 | -5.4% |
| **+15¢** | 26702 | 19864 | 6838 (112) | 2 | $-9958.50 | -5.9% |
| **+20¢** | 23712 | 16545 | 7167 (145) | 2 | $-8830.14 | -5.9% |
| **+10¢ (15¢ stop)** | 52213 | 52130 | 83 (48) | 2 | $-19786.82 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 22:00 | +10 stop | HYPE | UP | 0.55 | open |  |
| 10-31 22:00 | +20 | HYPE | UP | 0.55 | open |  |
| 10-31 22:00 | +15 | HYPE | UP | 0.55 | open |  |
| 10-31 22:00 | +10 | HYPE | UP | 0.55 | open |  |
| 10-31 22:00 | +5 | HYPE | UP | 0.55 | open |  |
| 10-31 22:00 | +10 stop | ETH | UP | 0.64 | open |  |
| 10-31 22:00 | +20 | ETH | UP | 0.64 | open |  |
| 10-31 22:00 | +15 | ETH | UP | 0.64 | open |  |
| 10-31 22:00 | +10 | ETH | UP | 0.64 | open |  |
| 10-31 22:00 | +5 | ETH | UP | 0.64 | 0.73 | 0.59 |
| 10-31 21:58 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-31 21:58 | +20 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 10-31 21:58 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 21:58 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-31 21:57 | +10 stop | DOGE | UP | 0.56 | 0.72 | 1.27 |
| 10-31 21:57 | +10 stop | ZEC | UP | 0.62 | 0.83 | 1.83 |
| 10-31 21:54 | +10 stop | BNB | DOWN | 0.68 | 0.33 | -3.82 |
| 10-31 21:54 | +10 stop | XRP | DOWN | 0.54 | 0.78 | 2.09 |
| 10-31 21:54 | +10 stop | ETH | UP | 0.54 | 0.78 | 2.09 |
| 10-31 21:54 | +10 stop | SOL | DOWN | 0.64 | 0.30 | -3.72 |
| 10-31 21:54 | +5 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 10-31 21:53 | +10 stop | XRP | UP | 0.65 | 0.40 | -2.83 |
| 10-31 21:52 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-31 21:52 | +10 stop | BNB | UP | 0.65 | 0.43 | -2.54 |
| 10-31 21:51 | +10 | BNB | UP | 0.71 | 0.82 | 0.84 |
| 10-31 21:51 | +5 | BNB | UP | 0.71 | 0.80 | 0.63 |
| 10-31 21:51 | +15 | BNB | UP | 0.71 | 0.88 | 1.47 |
| 10-31 21:50 | +5 | ETH | UP | 0.70 | 0.78 | 0.52 |
| 10-31 21:50 | +5 | HYPE | UP | 0.68 | no | -6.96 |
| 10-31 21:49 | +5 | BNB | UP | 0.60 | 0.68 | 0.47 |
| 10-31 21:49 | +10 stop | BNB | UP | 0.55 | 0.68 | 0.96 |
| 10-31 21:49 | +10 | BNB | UP | 0.55 | 0.68 | 0.96 |
| 10-31 21:49 | +5 | BNB | UP | 0.55 | 0.62 | 0.35 |
| 10-31 21:49 | +5 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 21:48 | +10 stop | HYPE | UP | 0.70 | 0.42 | -3.13 |
| 10-31 21:48 | +10 stop | ZEC | DOWN | 0.70 | 0.50 | -2.31 |
| 10-31 21:48 | +20 | ZEC | DOWN | 0.70 | yes | -7.13 |
| 10-31 21:48 | +15 | ZEC | DOWN | 0.70 | yes | -7.13 |
| 10-31 21:48 | +10 | ZEC | DOWN | 0.70 | yes | -7.13 |
| 10-31 21:48 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.34 |
