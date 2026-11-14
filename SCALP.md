# Range-Scalp Bot

*Updated Sat Nov 14 22:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59944 | 52285 | 7659 (107) | 2 | $-16340.25 | -4.3% |
| **+10¢** | 44787 | 35821 | 8966 (143) | 7 | $-15377.54 | -5.5% |
| **+15¢** | 37520 | 27853 | 9667 (180) | 8 | $-14016.93 | -6.0% |
| **+20¢** | 33426 | 23284 | 10142 (232) | 8 | $-12359.10 | -5.9% |
| **+10¢ (15¢ stop)** | 72977 | 72834 | 143 (82) | 0 | $-26819.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 22:21 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 11-14 22:20 | +10 stop | BTC | UP | 0.60 | 0.78 | 1.50 |
| 11-14 22:20 | +10 stop | BNB | UP | 0.65 | 0.80 | 1.22 |
| 11-14 22:19 | +10 stop | BTC | UP | 0.56 | 0.41 | -1.85 |
| 11-14 22:19 | +10 stop | DOGE | UP | 0.67 | 0.84 | 1.44 |
| 11-14 22:19 | +5 | DOGE | UP | 0.67 | 0.76 | 0.61 |
| 11-14 22:19 | +10 stop | SOL | UP | 0.63 | 0.82 | 1.62 |
| 11-14 22:18 | +10 stop | ETH | UP | 0.67 | 0.83 | 1.34 |
| 11-14 22:18 | +10 stop | BNB | UP | 0.63 | 0.43 | -2.35 |
| 11-14 22:18 | +10 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 11-14 22:18 | +5 | BNB | UP | 0.63 | 0.69 | 0.28 |
| 11-14 22:18 | +5 | ETH | UP | 0.69 | 0.75 | 0.31 |
| 11-14 22:18 | +10 stop | BNB | DOWN | 0.47 | 0.59 | 0.85 |
| 11-14 22:18 | +10 | BNB | DOWN | 0.49 | 0.59 | 0.66 |
| 11-14 22:18 | +5 | BNB | DOWN | 0.49 | 0.59 | 0.68 |
| 11-14 22:18 | +10 stop | DOGE | DOWN | 0.46 | 0.26 | -2.32 |
| 11-14 22:18 | +10 | DOGE | DOWN | 0.48 | open |  |
| 11-14 22:18 | +5 | DOGE | DOWN | 0.49 | 0.54 | 0.14 |
| 11-14 22:18 | +5 | ETH | DOWN | 0.42 | 0.55 | 0.94 |
| 11-14 22:17 | +10 stop | BTC | DOWN | 0.60 | 0.42 | -2.15 |
| 11-14 22:17 | +10 | BTC | DOWN | 0.60 | open |  |
| 11-14 22:17 | +5 | BTC | DOWN | 0.60 | open |  |
| 11-14 22:17 | +5 | ETH | DOWN | 0.54 | 0.63 | 0.55 |
| 11-14 22:17 | +5 | XRP | DOWN | 0.58 | 0.66 | 0.46 |
| 11-14 22:17 | +10 stop | HYPE | DOWN | 0.49 | 0.07 | -4.41 |
| 11-14 22:17 | +15 | HYPE | DOWN | 0.49 | open |  |
| 11-14 22:17 | +10 | HYPE | DOWN | 0.49 | open |  |
| 11-14 22:17 | +5 | HYPE | DOWN | 0.49 | 0.55 | 0.24 |
| 11-14 22:17 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-14 22:16 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
| 11-14 22:16 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-14 22:16 | +15 | NEAR | DOWN | 0.65 | open |  |
| 11-14 22:16 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-14 22:16 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 11-14 22:16 | +10 stop | BNB | DOWN | 0.69 | 0.82 | 1.05 |
| 11-14 22:16 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-14 22:16 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-14 22:16 | +10 | BNB | DOWN | 0.69 | 0.82 | 1.05 |
| 11-14 22:16 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.30 |
| 11-14 22:16 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
