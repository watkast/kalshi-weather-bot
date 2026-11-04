# Range-Scalp Bot

*Updated Wed Nov 04 19:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47416 | 41292 | 6124 (72) | 3 | $-13645.38 | -4.6% |
| **+10¢** | 35418 | 28312 | 7106 (97) | 3 | $-12484.88 | -5.6% |
| **+15¢** | 29660 | 22008 | 7652 (125) | 3 | $-11454.39 | -6.2% |
| **+20¢** | 26350 | 18337 | 8013 (165) | 4 | $-10101.09 | -6.1% |
| **+10¢ (15¢ stop)** | 57788 | 57695 | 93 (56) | 0 | $-21542.09 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 18:59 | +10 stop | BTC | DOWN | 0.49 | 0.95 | 4.42 |
| 11-04 18:59 | +20 | BTC | DOWN | 0.49 | 0.95 | 4.42 |
| 11-04 18:59 | +15 | BTC | DOWN | 0.50 | 0.95 | 4.32 |
| 11-04 18:59 | +10 | BTC | DOWN | 0.50 | 0.95 | 4.32 |
| 11-04 18:59 | +5 | BTC | DOWN | 0.50 | 0.57 | 0.34 |
| 11-04 18:58 | +10 stop | BNB | DOWN | 0.59 | 0.12 | -4.95 |
| 11-04 18:57 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-04 18:56 | +10 stop | BNB | DOWN | 0.71 | 0.52 | -2.23 |
| 11-04 18:56 | +10 stop | BTC | DOWN | 0.67 | 0.48 | -2.24 |
| 11-04 18:56 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-04 18:56 | +15 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-04 18:56 | +10 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-04 18:56 | +5 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-04 18:55 | +10 stop | ZEC | UP | 0.56 | 0.75 | 1.58 |
| 11-04 18:55 | +10 stop | ETH | DOWN | 0.66 | 0.36 | -3.33 |
| 11-04 18:55 | +10 stop | HYPE | UP | 0.71 | 0.84 | 1.05 |
| 11-04 18:55 | +20 | HYPE | UP | 0.71 | 0.92 | 1.89 |
| 11-04 18:55 | +15 | HYPE | UP | 0.71 | 0.90 | 1.69 |
| 11-04 18:55 | +10 | HYPE | UP | 0.71 | 0.84 | 1.05 |
| 11-04 18:55 | +5 | HYPE | UP | 0.71 | 0.77 | 0.32 |
| 11-04 18:55 | +10 stop | ZEC | DOWN | 0.64 | 0.45 | -2.25 |
| 11-04 18:55 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-04 18:54 | +10 stop | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-04 18:54 | +10 stop | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-04 18:54 | +20 | BTC | DOWN | 0.52 | 0.77 | 2.19 |
| 11-04 18:54 | +15 | BTC | DOWN | 0.52 | 0.70 | 1.47 |
| 11-04 18:54 | +10 | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-04 18:54 | +5 | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-04 18:54 | +10 stop | ETH | UP | 0.61 | 0.30 | -3.42 |
| 11-04 18:54 | +15 | ETH | UP | 0.61 | 0.79 | 1.51 |
| 11-04 18:54 | +10 | ETH | UP | 0.61 | 0.79 | 1.51 |
| 11-04 18:54 | +5 | ETH | UP | 0.61 | 0.79 | 1.51 |
| 11-04 18:54 | +10 stop | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 11-04 18:54 | +15 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 11-04 18:54 | +10 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 11-04 18:54 | +5 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 11-04 18:54 | +10 | ZEC | DOWN | 0.57 | open |  |
| 11-04 18:54 | +5 | ZEC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-04 18:54 | +10 stop | BNB | UP | 0.68 | 0.53 | -1.84 |
| 11-04 18:54 | +20 | BNB | UP | 0.68 | 0.96 | 2.61 |
