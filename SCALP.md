# Range-Scalp Bot

*Updated Tue Nov 24 19:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70951 | 61932 | 9019 (155) | 7 | $-18886.62 | -4.2% |
| **+10¢** | 52924 | 42391 | 10533 (201) | 8 | $-17481.22 | -5.3% |
| **+15¢** | 44326 | 32979 | 11347 (258) | 7 | $-15581.15 | -5.6% |
| **+20¢** | 39465 | 27520 | 11945 (324) | 7 | $-13948.10 | -5.6% |
| **+10¢ (15¢ stop)** | 86383 | 86182 | 201 (121) | 2 | $-31750.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 19:24 | +10 stop | DOGE | UP | 0.55 | open |  |
| 11-24 19:24 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-24 19:23 | +10 stop | NEAR | UP | 0.68 | 0.85 | 1.45 |
| 11-24 19:22 | +10 stop | DOGE | DOWN | 0.67 | 0.48 | -2.24 |
| 11-24 19:22 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-24 19:22 | +15 | NEAR | UP | 0.59 | 0.77 | 1.55 |
| 11-24 19:22 | +10 stop | HYPE | DOWN | 0.70 | 0.55 | -1.83 |
| 11-24 19:21 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-24 19:21 | +5 | NEAR | UP | 0.71 | 0.77 | 0.32 |
| 11-24 19:21 | +5 | XRP | UP | 0.59 | open |  |
| 11-24 19:20 | +10 stop | SOL | UP | 0.62 | 0.44 | -2.15 |
| 11-24 19:20 | +10 stop | BTC | UP | 0.50 | 0.32 | -2.14 |
| 11-24 19:20 | +10 stop | DOGE | UP | 0.58 | 0.30 | -3.13 |
| 11-24 19:20 | +10 | NEAR | DOWN | 0.54 | open |  |
| 11-24 19:20 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 11-24 19:19 | +10 stop | XRP | UP | 0.64 | 0.33 | -3.48 |
| 11-24 19:19 | +20 | XRP | UP | 0.64 | open |  |
| 11-24 19:19 | +15 | XRP | UP | 0.64 | open |  |
| 11-24 19:19 | +10 | XRP | UP | 0.64 | open |  |
| 11-24 19:19 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 11-24 19:19 | +10 stop | NEAR | UP | 0.54 | 0.70 | 1.27 |
| 11-24 19:19 | +20 | NEAR | UP | 0.52 | 0.73 | 1.78 |
| 11-24 19:19 | +15 | NEAR | UP | 0.47 | 0.70 | 1.97 |
| 11-24 19:19 | +10 | NEAR | UP | 0.47 | 0.58 | 0.74 |
| 11-24 19:19 | +5 | NEAR | UP | 0.47 | 0.58 | 0.74 |
| 11-24 19:17 | +10 stop | SOL | UP | 0.66 | 0.46 | -2.34 |
| 11-24 19:17 | +20 | SOL | UP | 0.66 | open |  |
| 11-24 19:17 | +15 | SOL | UP | 0.66 | open |  |
| 11-24 19:17 | +10 | SOL | UP | 0.66 | open |  |
| 11-24 19:17 | +5 | SOL | UP | 0.66 | open |  |
| 11-24 19:17 | +10 stop | ETH | UP | 0.60 | 0.41 | -2.24 |
| 11-24 19:17 | +20 | ETH | UP | 0.60 | open |  |
| 11-24 19:17 | +15 | ETH | UP | 0.60 | open |  |
| 11-24 19:17 | +10 | ETH | UP | 0.60 | open |  |
| 11-24 19:17 | +5 | ETH | UP | 0.60 | open |  |
| 11-24 19:17 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 11-24 19:17 | +20 | BTC | UP | 0.61 | open |  |
| 11-24 19:17 | +15 | BTC | UP | 0.61 | open |  |
| 11-24 19:17 | +10 | BTC | UP | 0.61 | open |  |
| 11-24 19:17 | +5 | BTC | UP | 0.61 | open |  |
