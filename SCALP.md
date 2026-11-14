# Range-Scalp Bot

*Updated Sat Nov 14 20:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59846 | 52217 | 7629 (107) | 7 | $-16181.36 | -4.3% |
| **+10¢** | 44713 | 35779 | 8934 (143) | 7 | $-15215.52 | -5.4% |
| **+15¢** | 37459 | 27825 | 9634 (180) | 7 | $-13853.24 | -5.9% |
| **+20¢** | 33369 | 23260 | 10109 (232) | 7 | $-12202.15 | -5.8% |
| **+10¢ (15¢ stop)** | 72836 | 72693 | 143 (82) | 0 | $-26730.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 20:50 | +10 stop | ETH | UP | 0.49 | 0.33 | -1.94 |
| 11-14 20:49 | +10 stop | DOGE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-14 20:49 | +10 stop | BTC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-14 20:49 | +10 stop | BNB | DOWN | 0.60 | 0.79 | 1.61 |
| 11-14 20:49 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-14 20:49 | +10 stop | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 11-14 20:48 | +10 stop | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-14 20:48 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-14 20:48 | +15 | ZEC | DOWN | 0.65 | 0.83 | 1.54 |
| 11-14 20:48 | +10 | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-14 20:48 | +5 | ZEC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-14 20:48 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-14 20:48 | +20 | HYPE | DOWN | 0.61 | 0.86 | 2.24 |
| 11-14 20:48 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-14 20:48 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 20:48 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-14 20:48 | +10 stop | ETH | UP | 0.64 | 0.47 | -2.05 |
| 11-14 20:48 | +10 | ETH | UP | 0.64 | open |  |
| 11-14 20:47 | +5 | ETH | UP | 0.69 | open |  |
| 11-14 20:47 | +5 | BTC | UP | 0.64 | open |  |
| 11-14 20:46 | +10 stop | BNB | UP | 0.59 | 0.39 | -2.34 |
| 11-14 20:46 | +20 | BNB | UP | 0.59 | open |  |
| 11-14 20:46 | +15 | BNB | UP | 0.59 | open |  |
| 11-14 20:46 | +10 | BNB | UP | 0.59 | open |  |
| 11-14 20:46 | +5 | BNB | UP | 0.59 | open |  |
| 11-14 20:46 | +10 stop | XRP | UP | 0.55 | 0.35 | -2.34 |
| 11-14 20:46 | +20 | XRP | UP | 0.55 | open |  |
| 11-14 20:46 | +15 | XRP | UP | 0.55 | open |  |
| 11-14 20:46 | +10 | XRP | UP | 0.56 | open |  |
| 11-14 20:46 | +5 | XRP | UP | 0.56 | open |  |
| 11-14 20:45 | +10 stop | NEAR | UP | 0.59 | 0.33 | -2.93 |
| 11-14 20:45 | +20 | NEAR | UP | 0.59 | open |  |
| 11-14 20:45 | +15 | NEAR | UP | 0.59 | open |  |
| 11-14 20:45 | +10 | NEAR | UP | 0.59 | open |  |
| 11-14 20:45 | +5 | NEAR | UP | 0.59 | open |  |
| 11-14 20:45 | +10 stop | DOGE | UP | 0.58 | 0.41 | -2.05 |
| 11-14 20:45 | +20 | DOGE | UP | 0.58 | open |  |
| 11-14 20:45 | +15 | DOGE | UP | 0.58 | open |  |
| 11-14 20:45 | +10 | DOGE | UP | 0.58 | open |  |
| 11-14 20:45 | +5 | DOGE | UP | 0.58 | open |  |
