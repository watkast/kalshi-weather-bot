# Range-Scalp Bot

*Updated Sat Nov 14 10:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59357 | 51797 | 7560 (107) | 0 | $-15990.28 | -4.3% |
| **+10¢** | 44333 | 35483 | 8850 (142) | 0 | $-15009.20 | -5.4% |
| **+15¢** | 37151 | 27607 | 9544 (178) | 2 | $-13644.26 | -5.9% |
| **+20¢** | 33096 | 23079 | 10017 (230) | 2 | $-12013.95 | -5.8% |
| **+10¢ (15¢ stop)** | 72205 | 72063 | 142 (82) | 0 | $-26536.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 10:48 | +10 stop | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-14 10:48 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-14 10:48 | +5 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-14 10:45 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 10:45 | +20 | ZEC | DOWN | 0.70 | 0.92 | 1.97 |
| 11-14 10:45 | +15 | ZEC | DOWN | 0.70 | 0.92 | 1.97 |
| 11-14 10:45 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 10:45 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-14 10:45 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-14 10:45 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-14 10:45 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-14 10:45 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-14 10:45 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-14 10:45 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 10:45 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-14 10:45 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-14 10:45 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 10:45 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 11-14 10:40 | +10 stop | HYPE | DOWN | 0.64 | 0.45 | -2.25 |
| 11-14 10:40 | +20 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-14 10:40 | +15 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-14 10:40 | +10 | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-14 10:40 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-14 10:40 | +10 stop | BTC | UP | 0.58 | 0.42 | -1.96 |
| 11-14 10:39 | +10 | ETH | UP | 0.66 | 0.79 | 1.02 |
| 11-14 10:39 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 11-14 10:39 | +20 | NEAR | UP | 0.56 | 0.76 | 1.72 |
| 11-14 10:39 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.79 |
| 11-14 10:39 | +10 stop | NEAR | UP | 0.69 | 0.82 | 1.03 |
| 11-14 10:39 | +5 | NEAR | UP | 0.69 | 0.76 | 0.42 |
| 11-14 10:39 | +10 stop | BTC | UP | 0.56 | 0.66 | 0.66 |
| 11-14 10:39 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 11-14 10:38 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-14 10:38 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 11-14 10:38 | +10 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-14 10:38 | +5 | SOL | DOWN | 0.65 | yes | -6.66 |
| 11-14 10:37 | +5 | DOGE | DOWN | 0.54 | yes | -5.56 |
| 11-14 10:37 | +10 stop | ETH | DOWN | 0.63 | 0.47 | -1.95 |
| 11-14 10:37 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 11-14 10:36 | +10 stop | DOGE | DOWN | 0.62 | 0.34 | -3.13 |
