# Range-Scalp Bot

*Updated Thu Nov 19 18:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65318 | 57027 | 8291 (124) | 4 | $-17421.50 | -4.2% |
| **+10¢** | 48777 | 39074 | 9703 (165) | 5 | $-16230.65 | -5.3% |
| **+15¢** | 40898 | 30431 | 10467 (211) | 4 | $-14622.58 | -5.7% |
| **+20¢** | 36418 | 25422 | 10996 (266) | 6 | $-12937.54 | -5.7% |
| **+10¢ (15¢ stop)** | 79509 | 79345 | 164 (98) | 2 | $-29259.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 18:11 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-19 18:11 | +10 | ETH | UP | 0.61 | open |  |
| 11-19 18:11 | +5 | ETH | UP | 0.60 | open |  |
| 11-19 18:11 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 11-19 18:11 | +5 | SOL | DOWN | 0.71 | open |  |
| 11-19 18:11 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-19 18:11 | +15 | BTC | DOWN | 0.64 | 0.81 | 1.42 |
| 11-19 18:11 | +5 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-19 18:10 | +10 stop | BNB | UP | 0.52 | 0.69 | 1.37 |
| 11-19 18:10 | +15 | BNB | UP | 0.52 | 0.69 | 1.37 |
| 11-19 18:10 | +5 | BNB | UP | 0.54 | 0.69 | 1.17 |
| 11-19 18:10 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-19 18:10 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-19 18:10 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 18:10 | +10 stop | BTC | UP | 0.43 | 0.62 | 1.55 |
| 11-19 18:10 | +15 | BTC | UP | 0.43 | 0.62 | 1.55 |
| 11-19 18:10 | +5 | BTC | UP | 0.43 | 0.62 | 1.55 |
| 11-19 18:10 | +10 stop | XRP | UP | 0.36 | 0.53 | 1.35 |
| 11-19 18:10 | +20 | XRP | UP | 0.35 | open |  |
| 11-19 18:10 | +15 | XRP | UP | 0.36 | 0.53 | 1.35 |
| 11-19 18:10 | +10 | XRP | UP | 0.37 | 0.53 | 1.25 |
| 11-19 18:09 | +10 stop | BTC | DOWN | 0.41 | 0.58 | 1.35 |
| 11-19 18:09 | +20 | BTC | DOWN | 0.41 | 0.65 | 2.07 |
| 11-19 18:09 | +15 | BTC | DOWN | 0.42 | 0.58 | 1.24 |
| 11-19 18:09 | +5 | BTC | DOWN | 0.45 | 0.58 | 0.94 |
| 11-19 18:09 | +15 | BNB | DOWN | 0.49 | 0.67 | 1.46 |
| 11-19 18:09 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-19 18:09 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-19 18:08 | +10 | BNB | DOWN | 0.70 | open |  |
| 11-19 18:08 | +10 stop | DOGE | DOWN | 0.67 | 0.37 | -3.33 |
| 11-19 18:08 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 11-19 18:08 | +10 stop | NEAR | DOWN | 0.61 | 0.25 | -3.89 |
| 11-19 18:08 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.19 |
| 11-19 18:07 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.24 |
| 11-19 18:07 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 11-19 18:07 | +10 stop | DOGE | UP | 0.51 | 0.35 | -1.94 |
| 11-19 18:07 | +10 stop | ETH | UP | 0.56 | 0.68 | 0.86 |
| 11-19 18:07 | +5 | DOGE | UP | 0.56 | 0.75 | 1.58 |
| 11-19 18:06 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
| 11-19 18:06 | +10 stop | BNB | DOWN | 0.36 | 0.55 | 1.55 |
