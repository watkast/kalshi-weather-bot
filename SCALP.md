# Range-Scalp Bot

*Updated Wed Nov 18 04:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63602 | 55469 | 8133 (118) | 3 | $-17395.73 | -4.3% |
| **+10¢** | 47516 | 37996 | 9520 (159) | 3 | $-16325.95 | -5.5% |
| **+15¢** | 39844 | 29579 | 10265 (204) | 3 | $-14800.67 | -5.9% |
| **+20¢** | 35489 | 24716 | 10773 (259) | 3 | $-13070.35 | -5.9% |
| **+10¢ (15¢ stop)** | 77388 | 77230 | 158 (93) | 3 | $-28440.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 04:46 | +10 stop | DOGE | DOWN | 0.59 | open |  |
| 11-18 04:46 | +20 | DOGE | DOWN | 0.59 | open |  |
| 11-18 04:46 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-18 04:46 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-18 04:46 | +5 | DOGE | DOWN | 0.58 | open |  |
| 11-18 04:46 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 11-18 04:46 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-18 04:46 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-18 04:46 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-18 04:46 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-18 04:45 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-18 04:45 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-18 04:45 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-18 04:45 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-18 04:45 | +5 | ZEC | DOWN | 0.61 | open |  |
| 11-18 04:39 | +10 stop | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-18 04:39 | +5 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-18 04:38 | +5 | SOL | UP | 0.45 | 0.56 | 0.74 |
| 11-18 04:38 | +10 stop | SOL | UP | 0.45 | 0.56 | 0.74 |
| 11-18 04:37 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 04:35 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-18 04:34 | +10 stop | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-18 04:34 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-18 04:33 | +10 stop | XRP | UP | 0.53 | 0.35 | -2.14 |
| 11-18 04:33 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.35 |
| 11-18 04:33 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-18 04:32 | +10 stop | HYPE | DOWN | 0.56 | 0.79 | 2.00 |
| 11-18 04:32 | +10 stop | DOGE | DOWN | 0.57 | 0.72 | 1.17 |
| 11-18 04:32 | +20 | DOGE | DOWN | 0.57 | 0.77 | 1.69 |
| 11-18 04:32 | +15 | DOGE | DOWN | 0.57 | 0.72 | 1.17 |
| 11-18 04:32 | +10 | DOGE | DOWN | 0.58 | 0.72 | 1.07 |
| 11-18 04:32 | +5 | DOGE | DOWN | 0.58 | 0.63 | 0.15 |
| 11-18 04:32 | +10 stop | BTC | UP | 0.56 | 0.40 | -1.95 |
| 11-18 04:32 | +20 | BTC | UP | 0.56 | no | -5.78 |
| 11-18 04:32 | +15 | BTC | UP | 0.56 | no | -5.78 |
| 11-18 04:32 | +10 | BTC | UP | 0.55 | no | -5.68 |
| 11-18 04:32 | +5 | BTC | UP | 0.55 | no | -5.68 |
| 11-18 04:32 | +10 stop | ETH | UP | 0.52 | 0.36 | -1.95 |
| 11-18 04:32 | +20 | ETH | UP | 0.52 | no | -5.38 |
| 11-18 04:32 | +15 | ETH | UP | 0.51 | no | -5.28 |
