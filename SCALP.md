# Range-Scalp Bot

*Updated Wed Nov 11 15:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56016 | 48844 | 7172 (94) | 0 | $-15356.83 | -4.4% |
| **+10¢** | 41853 | 33488 | 8365 (124) | 0 | $-14308.89 | -5.4% |
| **+15¢** | 35089 | 26069 | 9020 (158) | 4 | $-13051.93 | -5.9% |
| **+20¢** | 31252 | 21790 | 9462 (208) | 6 | $-11424.92 | -5.8% |
| **+10¢ (15¢ stop)** | 68248 | 68127 | 121 (73) | 0 | $-25140.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 15:17 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-11 15:17 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-11 15:17 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-11 15:17 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-11 15:17 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-11 15:16 | +10 stop | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-11 15:16 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-11 15:16 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-11 15:16 | +10 | SOL | DOWN | 0.70 | 0.85 | 1.21 |
| 11-11 15:16 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.37 |
| 11-11 15:16 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-11 15:16 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-11 15:16 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-11 15:16 | +10 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-11 15:16 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-11 15:16 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-11 15:16 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-11 15:16 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-11 15:16 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-11 15:16 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 11-11 15:16 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 15:16 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-11 15:16 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-11 15:16 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 15:16 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-11 15:16 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-11 15:16 | +20 | ZEC | DOWN | 0.68 | 0.90 | 1.97 |
| 11-11 15:16 | +15 | ZEC | DOWN | 0.68 | 0.85 | 1.45 |
| 11-11 15:16 | +10 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-11 15:16 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 11-11 15:16 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-11 15:16 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-11 15:16 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-11 15:16 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-11 15:16 | +5 | NEAR | DOWN | 0.68 | 0.75 | 0.40 |
| 11-11 15:11 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
| 11-11 15:10 | +10 stop | HYPE | UP | 0.58 | 0.69 | 0.77 |
| 11-11 15:10 | +10 stop | BTC | DOWN | 0.68 | 0.46 | -2.54 |
| 11-11 15:10 | +5 | BTC | DOWN | 0.60 | yes | -6.17 |
| 11-11 15:10 | +10 stop | BNB | DOWN | 0.67 | 0.47 | -2.34 |
