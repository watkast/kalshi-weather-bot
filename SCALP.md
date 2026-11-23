# Range-Scalp Bot

*Updated Mon Nov 23 23:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70281 | 61337 | 8944 (147) | 2 | $-18845.82 | -4.3% |
| **+10¢** | 52436 | 41990 | 10446 (190) | 2 | $-17488.08 | -5.3% |
| **+15¢** | 43927 | 32677 | 11250 (246) | 5 | $-15581.01 | -5.7% |
| **+20¢** | 39110 | 27269 | 11841 (311) | 5 | $-13959.60 | -5.7% |
| **+10¢ (15¢ stop)** | 85597 | 85401 | 196 (118) | 2 | $-31490.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 23:31 | +5 | HYPE | UP | 0.59 | open |  |
| 11-23 23:30 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 11-23 23:30 | +20 | BTC | DOWN | 0.64 | open |  |
| 11-23 23:30 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-23 23:30 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-23 23:30 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-23 23:30 | +10 stop | XRP | UP | 0.42 | 0.54 | 0.84 |
| 11-23 23:30 | +20 | XRP | UP | 0.42 | open |  |
| 11-23 23:30 | +15 | XRP | UP | 0.42 | open |  |
| 11-23 23:30 | +10 | XRP | UP | 0.42 | 0.54 | 0.84 |
| 11-23 23:30 | +5 | XRP | UP | 0.41 | 0.54 | 0.95 |
| 11-23 23:30 | +10 stop | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-23 23:30 | +20 | DOGE | UP | 0.47 | open |  |
| 11-23 23:30 | +15 | DOGE | UP | 0.47 | open |  |
| 11-23 23:30 | +10 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-23 23:30 | +5 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-23 23:30 | +10 stop | BNB | UP | 0.46 | 0.56 | 0.64 |
| 11-23 23:30 | +20 | BNB | UP | 0.46 | open |  |
| 11-23 23:30 | +15 | BNB | UP | 0.46 | open |  |
| 11-23 23:30 | +10 | BNB | UP | 0.46 | 0.56 | 0.64 |
| 11-23 23:30 | +5 | BNB | UP | 0.47 | 0.56 | 0.54 |
| 11-23 23:30 | +10 stop | HYPE | UP | 0.57 | open |  |
| 11-23 23:30 | +20 | HYPE | UP | 0.57 | open |  |
| 11-23 23:30 | +15 | HYPE | UP | 0.57 | open |  |
| 11-23 23:30 | +10 | HYPE | UP | 0.57 | open |  |
| 11-23 23:30 | +5 | HYPE | UP | 0.57 | 0.62 | 0.15 |
| 11-23 23:27 | +10 stop | ETH | UP | 0.34 | 0.56 | 1.86 |
| 11-23 23:27 | +10 | ETH | UP | 0.34 | 0.56 | 1.86 |
| 11-23 23:27 | +5 | ETH | UP | 0.34 | 0.56 | 1.86 |
| 11-23 23:25 | +10 stop | DOGE | DOWN | 0.55 | 0.38 | -2.02 |
| 11-23 23:25 | +20 | DOGE | DOWN | 0.54 | yes | -5.55 |
| 11-23 23:25 | +15 | DOGE | DOWN | 0.52 | yes | -5.38 |
| 11-23 23:25 | +5 | DOGE | DOWN | 0.52 | 0.57 | 0.14 |
| 11-23 23:25 | +10 stop | HYPE | DOWN | 0.43 | 0.56 | 0.94 |
| 11-23 23:25 | +10 stop | SOL | DOWN | 0.39 | 0.54 | 1.17 |
| 11-23 23:24 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-23 23:24 | +20 | NEAR | UP | 0.57 | 0.82 | 2.21 |
| 11-23 23:24 | +15 | NEAR | UP | 0.57 | 0.82 | 2.21 |
| 11-23 23:24 | +10 | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-23 23:24 | +5 | NEAR | UP | 0.57 | 0.68 | 0.76 |
