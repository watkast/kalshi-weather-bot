# Range-Scalp Bot

*Updated Thu Nov 12 03:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56594 | 49336 | 7258 (98) | 5 | $-15588.94 | -4.4% |
| **+10¢** | 42287 | 33820 | 8467 (128) | 6 | $-14542.12 | -5.5% |
| **+15¢** | 35455 | 26337 | 9118 (162) | 8 | $-13204.80 | -5.9% |
| **+20¢** | 31588 | 22019 | 9569 (212) | 8 | $-11599.82 | -5.9% |
| **+10¢ (15¢ stop)** | 68991 | 68868 | 123 (73) | 2 | $-25476.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 03:54 | +5 | ZEC | UP | 0.48 | 0.55 | 0.34 |
| 11-12 03:54 | +10 stop | HYPE | UP | 0.71 | 0.49 | -2.53 |
| 11-12 03:54 | +10 | HYPE | UP | 0.71 | open |  |
| 11-12 03:54 | +5 | HYPE | UP | 0.71 | open |  |
| 11-12 03:54 | +10 stop | SOL | UP | 0.68 | open |  |
| 11-12 03:54 | +20 | SOL | UP | 0.68 | open |  |
| 11-12 03:54 | +15 | SOL | UP | 0.68 | open |  |
| 11-12 03:54 | +10 | SOL | UP | 0.67 | open |  |
| 11-12 03:54 | +5 | SOL | UP | 0.68 | open |  |
| 11-12 03:54 | +5 | ZEC | UP | 0.55 | 0.60 | 0.15 |
| 11-12 03:53 | +10 stop | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 11-12 03:53 | +10 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 11-12 03:53 | +5 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 11-12 03:52 | +10 stop | NEAR | DOWN | 0.61 | 0.75 | 1.09 |
| 11-12 03:52 | +10 stop | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-12 03:52 | +10 | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-12 03:52 | +5 | BNB | DOWN | 0.71 | 0.79 | 0.53 |
| 11-12 03:52 | +10 stop | DOGE | UP | 0.59 | 0.32 | -3.03 |
| 11-12 03:52 | +20 | DOGE | UP | 0.59 | open |  |
| 11-12 03:52 | +15 | DOGE | UP | 0.59 | open |  |
| 11-12 03:52 | +10 | DOGE | UP | 0.59 | open |  |
| 11-12 03:52 | +5 | DOGE | UP | 0.59 | open |  |
| 11-12 03:52 | +10 stop | ZEC | UP | 0.55 | open |  |
| 11-12 03:52 | +15 | ZEC | UP | 0.55 | open |  |
| 11-12 03:52 | +10 | ZEC | UP | 0.55 | open |  |
| 11-12 03:52 | +5 | ZEC | UP | 0.55 | 0.60 | 0.15 |
| 11-12 03:51 | +10 stop | ETH | UP | 0.71 | 0.47 | -2.73 |
| 11-12 03:51 | +20 | ETH | UP | 0.71 | open |  |
| 11-12 03:51 | +15 | ETH | UP | 0.71 | open |  |
| 11-12 03:51 | +10 | ETH | UP | 0.71 | open |  |
| 11-12 03:51 | +5 | ETH | UP | 0.71 | open |  |
| 11-12 03:51 | +5 | BNB | DOWN | 0.54 | 0.63 | 0.55 |
| 11-12 03:51 | +10 stop | HYPE | UP | 0.69 | 0.82 | 1.04 |
| 11-12 03:51 | +20 | HYPE | UP | 0.69 | open |  |
| 11-12 03:51 | +15 | HYPE | UP | 0.69 | open |  |
| 11-12 03:51 | +10 | HYPE | UP | 0.69 | 0.82 | 1.04 |
| 11-12 03:51 | +5 | HYPE | UP | 0.69 | 0.82 | 1.04 |
| 11-12 03:51 | +10 stop | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-12 03:51 | +10 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-12 03:51 | +5 | BNB | DOWN | 0.53 | 0.58 | 0.14 |
