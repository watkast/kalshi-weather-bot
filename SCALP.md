# Range-Scalp Bot

*Updated Wed Oct 07 05:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5999 | 5205 | 794 (9) | 6 | $-1819.51 | -4.8% |
| **+10¢** | 4577 | 3642 | 935 (16) | 6 | $-1700.56 | -5.9% |
| **+15¢** | 3846 | 2855 | 991 (20) | 6 | $-1464.03 | -6.1% |
| **+20¢** | 3433 | 2397 | 1036 (27) | 6 | $-1213.16 | -5.6% |
| **+10¢ (15¢ stop)** | 7292 | 7277 | 15 (9) | 0 | $-2523.93 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 05:24 | +10 stop | ZEC | DOWN | 0.41 | 0.57 | 1.25 |
| 10-07 05:21 | +10 stop | XRP | UP | 0.69 | 0.82 | 0.99 |
| 10-07 05:21 | +10 stop | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-07 05:21 | +10 stop | ETH | DOWN | 0.55 | 0.38 | -2.05 |
| 10-07 05:19 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 10-07 05:19 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 10-07 05:19 | +10 stop | DOGE | UP | 0.67 | 0.81 | 1.13 |
| 10-07 05:19 | +10 | DOGE | UP | 0.67 | 0.81 | 1.13 |
| 10-07 05:19 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-07 05:19 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 10-07 05:18 | +5 | DOGE | UP | 0.65 | 0.72 | 0.39 |
| 10-07 05:18 | +5 | XRP | DOWN | 0.55 | open |  |
| 10-07 05:17 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-07 05:17 | +20 | DOGE | UP | 0.53 | 0.74 | 1.78 |
| 10-07 05:17 | +15 | DOGE | UP | 0.53 | 0.68 | 1.16 |
| 10-07 05:17 | +10 | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-07 05:17 | +5 | DOGE | UP | 0.53 | 0.59 | 0.25 |
| 10-07 05:17 | +10 stop | ETH | DOWN | 0.58 | 0.42 | -1.96 |
| 10-07 05:17 | +20 | ETH | DOWN | 0.58 | open |  |
| 10-07 05:17 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-07 05:17 | +10 | ETH | DOWN | 0.58 | open |  |
| 10-07 05:17 | +5 | ETH | DOWN | 0.58 | open |  |
| 10-07 05:17 | +10 stop | SOL | DOWN | 0.59 | 0.44 | -1.85 |
| 10-07 05:17 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-07 05:17 | +15 | SOL | DOWN | 0.59 | open |  |
| 10-07 05:17 | +10 | SOL | DOWN | 0.59 | open |  |
| 10-07 05:17 | +5 | SOL | DOWN | 0.59 | open |  |
| 10-07 05:17 | +10 stop | HYPE | DOWN | 0.59 | 0.35 | -2.73 |
| 10-07 05:17 | +20 | HYPE | DOWN | 0.59 | open |  |
| 10-07 05:17 | +15 | HYPE | DOWN | 0.59 | open |  |
| 10-07 05:17 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-07 05:17 | +5 | HYPE | DOWN | 0.59 | open |  |
| 10-07 05:16 | +10 stop | XRP | DOWN | 0.60 | 0.42 | -2.15 |
| 10-07 05:16 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-07 05:16 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-07 05:16 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-07 05:16 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-07 05:16 | +10 stop | BTC | DOWN | 0.58 | 0.43 | -1.86 |
| 10-07 05:16 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-07 05:16 | +15 | BTC | DOWN | 0.58 | open |  |
