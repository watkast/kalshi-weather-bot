# Range-Scalp Bot

*Updated Mon Oct 26 23:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35599 | 31065 | 4534 (43) | 3 | $-9985.35 | -4.5% |
| **+10¢** | 26618 | 21375 | 5243 (65) | 3 | $-8819.60 | -5.3% |
| **+15¢** | 22280 | 16641 | 5639 (89) | 2 | $-7890.34 | -5.6% |
| **+20¢** | 19756 | 13846 | 5910 (112) | 1 | $-6946.20 | -5.6% |
| **+10¢ (15¢ stop)** | 43644 | 43582 | 62 (33) | 0 | $-16622.56 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 23:34 | +10 stop | ZEC | UP | 0.71 | 0.81 | 0.74 |
| 10-26 23:33 | +5 | HYPE | UP | 0.68 | 0.77 | 0.61 |
| 10-26 23:33 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-26 23:33 | +5 | BNB | DOWN | 0.56 | open |  |
| 10-26 23:33 | +5 | NEAR | UP | 0.59 | 0.67 | 0.47 |
| 10-26 23:33 | +5 | HYPE | UP | 0.52 | 0.57 | 0.14 |
| 10-26 23:33 | +5 | XRP | UP | 0.39 | 0.61 | 1.86 |
| 10-26 23:33 | +10 stop | ETH | UP | 0.54 | 0.73 | 1.58 |
| 10-26 23:33 | +10 | ETH | UP | 0.54 | 0.73 | 1.58 |
| 10-26 23:33 | +5 | ETH | UP | 0.54 | 0.59 | 0.15 |
| 10-26 23:32 | +10 stop | BNB | DOWN | 0.60 | 0.42 | -2.16 |
| 10-26 23:32 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-26 23:32 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.46 |
| 10-26 23:32 | +10 stop | NEAR | DOWN | 0.53 | 0.31 | -2.53 |
| 10-26 23:32 | +20 | NEAR | DOWN | 0.53 | open |  |
| 10-26 23:32 | +15 | NEAR | DOWN | 0.53 | open |  |
| 10-26 23:32 | +10 | NEAR | DOWN | 0.53 | open |  |
| 10-26 23:32 | +5 | NEAR | DOWN | 0.53 | 0.60 | 0.35 |
| 10-26 23:32 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
| 10-26 23:32 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-26 23:32 | +10 | ZEC | DOWN | 0.59 | open |  |
| 10-26 23:32 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-26 23:32 | +10 stop | BTC | DOWN | 0.62 | 0.46 | -1.95 |
| 10-26 23:32 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-26 23:31 | +10 stop | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-26 23:31 | +20 | SOL | UP | 0.52 | 0.73 | 1.78 |
| 10-26 23:31 | +15 | SOL | UP | 0.52 | 0.73 | 1.78 |
| 10-26 23:31 | +10 | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-26 23:31 | +5 | SOL | UP | 0.53 | 0.58 | 0.14 |
| 10-26 23:31 | +5 | HYPE | UP | 0.53 | 0.58 | 0.14 |
| 10-26 23:31 | +10 stop | XRP | UP | 0.54 | 0.38 | -1.95 |
| 10-26 23:31 | +20 | XRP | UP | 0.54 | 0.82 | 2.51 |
| 10-26 23:31 | +15 | XRP | UP | 0.56 | 0.73 | 1.38 |
| 10-26 23:31 | +10 | XRP | UP | 0.56 | 0.73 | 1.38 |
| 10-26 23:31 | +5 | XRP | UP | 0.56 | 0.62 | 0.25 |
| 10-26 23:31 | +10 stop | ZEC | UP | 0.47 | 0.62 | 1.15 |
| 10-26 23:31 | +20 | ZEC | UP | 0.47 | 0.70 | 1.97 |
| 10-26 23:31 | +15 | ZEC | UP | 0.47 | 0.62 | 1.15 |
| 10-26 23:31 | +10 | ZEC | UP | 0.47 | 0.62 | 1.15 |
| 10-26 23:31 | +5 | ZEC | UP | 0.47 | 0.62 | 1.15 |
