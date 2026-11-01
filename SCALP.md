# Range-Scalp Bot

*Updated Sun Nov 01 19:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43822 | 38177 | 5645 (65) | 5 | $-12548.82 | -4.5% |
| **+10¢** | 32694 | 26171 | 6523 (86) | 5 | $-11300.06 | -5.5% |
| **+15¢** | 27364 | 20341 | 7023 (113) | 6 | $-10323.33 | -6.0% |
| **+20¢** | 24304 | 16948 | 7356 (147) | 6 | $-9111.44 | -6.0% |
| **+10¢ (15¢ stop)** | 53448 | 53362 | 86 (51) | 3 | $-20209.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 19:02 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 11-01 19:02 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-01 19:02 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-01 19:02 | +15 | BNB | DOWN | 0.65 | open |  |
| 11-01 19:02 | +10 | BNB | DOWN | 0.65 | open |  |
| 11-01 19:02 | +5 | BNB | DOWN | 0.65 | open |  |
| 11-01 19:02 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-01 19:02 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-01 19:02 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-01 19:02 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-01 19:02 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-01 19:01 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-01 19:01 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-01 19:01 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-01 19:01 | +10 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-01 19:01 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.40 |
| 11-01 19:01 | +10 stop | HYPE | UP | 0.65 | 0.25 | -4.34 |
| 11-01 19:01 | +20 | HYPE | UP | 0.65 | open |  |
| 11-01 19:01 | +15 | HYPE | UP | 0.65 | open |  |
| 11-01 19:01 | +10 | HYPE | UP | 0.65 | open |  |
| 11-01 19:01 | +5 | HYPE | UP | 0.65 | open |  |
| 11-01 19:01 | +10 stop | ETH | UP | 0.61 | 0.37 | -2.74 |
| 11-01 19:01 | +20 | ETH | UP | 0.61 | open |  |
| 11-01 19:01 | +15 | ETH | UP | 0.61 | open |  |
| 11-01 19:01 | +10 | ETH | UP | 0.61 | open |  |
| 11-01 19:01 | +5 | ETH | UP | 0.61 | open |  |
| 11-01 19:01 | +10 stop | SOL | UP | 0.55 | 0.31 | -2.73 |
| 11-01 19:01 | +20 | SOL | UP | 0.55 | open |  |
| 11-01 19:01 | +15 | SOL | UP | 0.55 | open |  |
| 11-01 19:01 | +10 | SOL | UP | 0.55 | open |  |
| 11-01 19:01 | +5 | SOL | UP | 0.55 | open |  |
| 11-01 19:01 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.93 |
| 11-01 19:01 | +20 | XRP | DOWN | 0.59 | 0.80 | 1.76 |
| 11-01 19:01 | +15 | XRP | DOWN | 0.59 | 0.80 | 1.76 |
| 11-01 19:01 | +10 | XRP | DOWN | 0.59 | 0.72 | 0.93 |
| 11-01 19:01 | +5 | XRP | DOWN | 0.59 | 0.72 | 0.93 |
| 11-01 18:49 | +10 stop | SOL | DOWN | 0.57 | 0.72 | 1.17 |
| 11-01 18:48 | +10 stop | BNB | DOWN | 0.62 | 0.90 | 2.51 |
| 11-01 18:48 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 18:48 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
