# Range-Scalp Bot

*Updated Thu Oct 15 11:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17383 | 15087 | 2296 (28) | 0 | $-5315.55 | -4.9% |
| **+10¢** | 13132 | 10473 | 2659 (40) | 0 | $-4837.33 | -5.9% |
| **+15¢** | 11032 | 8177 | 2855 (59) | 1 | $-4287.84 | -6.2% |
| **+20¢** | 9802 | 6816 | 2986 (77) | 2 | $-3720.72 | -6.0% |
| **+10¢ (15¢ stop)** | 21367 | 21317 | 50 (29) | 0 | $-8253.02 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 11:01 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 11:01 | +10 stop | XRP | DOWN | 0.64 | 0.77 | 0.98 |
| 10-15 11:01 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-15 11:01 | +15 | XRP | DOWN | 0.64 | 0.82 | 1.50 |
| 10-15 11:01 | +10 | XRP | DOWN | 0.64 | 0.77 | 0.96 |
| 10-15 11:01 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 10-15 11:00 | +10 stop | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-15 11:00 | +20 | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-15 11:00 | +15 | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 10-15 11:00 | +10 | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-15 11:00 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-15 11:00 | +10 stop | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-15 11:00 | +20 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-15 11:00 | +15 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-15 11:00 | +10 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-15 11:00 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.37 |
| 10-15 11:00 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-15 11:00 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-15 11:00 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-15 11:00 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-15 11:00 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-15 10:54 | +10 stop | ZEC | DOWN | 0.56 | 0.27 | -3.22 |
| 10-15 10:54 | +20 | ZEC | DOWN | 0.57 | yes | -5.91 |
| 10-15 10:54 | +15 | ZEC | DOWN | 0.57 | yes | -5.91 |
| 10-15 10:54 | +10 | ZEC | DOWN | 0.57 | yes | -5.91 |
| 10-15 10:54 | +5 | ZEC | DOWN | 0.57 | yes | -5.91 |
| 10-15 10:53 | +10 stop | BNB | DOWN | 0.67 | 0.47 | -2.33 |
| 10-15 10:53 | +10 | BNB | DOWN | 0.67 | yes | -6.85 |
| 10-15 10:53 | +5 | BNB | DOWN | 0.67 | yes | -6.85 |
| 10-15 10:53 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-15 10:53 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-15 10:52 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 10-15 10:51 | +10 stop | XRP | UP | 0.57 | 0.69 | 0.87 |
| 10-15 10:50 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 10-15 10:50 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.70 |
| 10-15 10:50 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 10-15 10:50 | +5 | SOL | DOWN | 0.63 | yes | -6.47 |
| 10-15 10:50 | +10 stop | BNB | DOWN | 0.69 | 0.83 | 1.14 |
| 10-15 10:50 | +5 | BNB | DOWN | 0.69 | 0.78 | 0.61 |
| 10-15 10:50 | +10 stop | DOGE | UP | 0.56 | 0.66 | 0.66 |
