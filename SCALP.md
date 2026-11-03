# Range-Scalp Bot

*Updated Tue Nov 03 11:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45848 | 39924 | 5924 (69) | 5 | $-13207.71 | -4.6% |
| **+10¢** | 34237 | 27371 | 6866 (91) | 6 | $-12084.26 | -5.6% |
| **+15¢** | 28650 | 21264 | 7386 (119) | 6 | $-11069.52 | -6.2% |
| **+20¢** | 25446 | 17705 | 7741 (155) | 6 | $-9852.25 | -6.2% |
| **+10¢ (15¢ stop)** | 55932 | 55843 | 89 (53) | 2 | $-20981.76 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 11:18 | +10 stop | BNB | DOWN | 0.59 | open |  |
| 11-03 11:18 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 11-03 11:18 | +5 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-03 11:18 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-03 11:17 | +10 stop | XRP | DOWN | 0.58 | 0.77 | 1.59 |
| 11-03 11:17 | +20 | XRP | DOWN | 0.58 | 0.80 | 1.90 |
| 11-03 11:17 | +15 | XRP | DOWN | 0.58 | 0.77 | 1.59 |
| 11-03 11:17 | +10 | XRP | DOWN | 0.58 | 0.77 | 1.59 |
| 11-03 11:17 | +5 | XRP | DOWN | 0.58 | 0.67 | 0.56 |
| 11-03 11:17 | +10 stop | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +20 | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +15 | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +10 | DOGE | DOWN | 0.51 | 0.74 | 1.98 |
| 11-03 11:17 | +5 | DOGE | DOWN | 0.51 | 0.57 | 0.24 |
| 11-03 11:17 | +10 stop | HYPE | UP | 0.54 | 0.37 | -2.05 |
| 11-03 11:17 | +20 | HYPE | UP | 0.54 | open |  |
| 11-03 11:17 | +15 | HYPE | UP | 0.54 | open |  |
| 11-03 11:17 | +10 | HYPE | UP | 0.54 | open |  |
| 11-03 11:17 | +5 | HYPE | UP | 0.54 | open |  |
| 11-03 11:16 | +10 stop | ZEC | UP | 0.48 | 0.29 | -2.23 |
| 11-03 11:16 | +20 | ZEC | UP | 0.48 | open |  |
| 11-03 11:16 | +15 | ZEC | UP | 0.48 | open |  |
| 11-03 11:16 | +10 | ZEC | UP | 0.48 | open |  |
| 11-03 11:16 | +5 | ZEC | UP | 0.48 | 0.53 | 0.14 |
| 11-03 11:16 | +10 stop | SOL | UP | 0.55 | 0.28 | -3.03 |
| 11-03 11:16 | +20 | SOL | UP | 0.56 | open |  |
| 11-03 11:16 | +15 | SOL | UP | 0.56 | open |  |
| 11-03 11:16 | +10 | SOL | UP | 0.56 | open |  |
| 11-03 11:16 | +5 | SOL | UP | 0.56 | open |  |
| 11-03 11:16 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.90 |
| 11-03 11:16 | +20 | BNB | UP | 0.60 | open |  |
| 11-03 11:16 | +15 | BNB | UP | 0.60 | open |  |
| 11-03 11:16 | +10 | BNB | UP | 0.60 | open |  |
| 11-03 11:16 | +5 | BNB | UP | 0.60 | open |  |
| 11-03 11:16 | +10 stop | BTC | UP | 0.58 | 0.37 | -2.45 |
| 11-03 11:16 | +20 | BTC | UP | 0.58 | open |  |
| 11-03 11:16 | +15 | BTC | UP | 0.58 | open |  |
| 11-03 11:16 | +10 | BTC | UP | 0.58 | open |  |
| 11-03 11:16 | +5 | BTC | UP | 0.58 | open |  |
| 11-03 11:16 | +10 stop | ETH | UP | 0.58 | 0.35 | -2.64 |
