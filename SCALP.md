# Range-Scalp Bot

*Updated Wed Nov 11 00:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55133 | 48089 | 7044 (94) | 5 | $-15006.52 | -4.3% |
| **+10¢** | 41193 | 32979 | 8214 (124) | 7 | $-13899.80 | -5.4% |
| **+15¢** | 34534 | 25681 | 8853 (158) | 7 | $-12632.39 | -5.8% |
| **+20¢** | 30744 | 21455 | 9289 (207) | 7 | $-11045.57 | -5.7% |
| **+10¢ (15¢ stop)** | 67163 | 67045 | 118 (73) | 5 | $-24769.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 00:35 | +10 stop | BNB | UP | 0.64 | open |  |
| 11-11 00:35 | +10 stop | SOL | UP | 0.64 | open |  |
| 11-11 00:35 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 11-11 00:35 | +10 | HYPE | DOWN | 0.56 | open |  |
| 11-11 00:35 | +5 | HYPE | DOWN | 0.54 | open |  |
| 11-11 00:35 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-11 00:35 | +5 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-11 00:34 | +5 | BTC | UP | 0.71 | open |  |
| 11-11 00:33 | +10 stop | BTC | UP | 0.67 | open |  |
| 11-11 00:33 | +10 stop | SOL | UP | 0.54 | 0.38 | -1.95 |
| 11-11 00:33 | +10 stop | ZEC | UP | 0.54 | open |  |
| 11-11 00:33 | +10 stop | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 00:33 | +20 | HYPE | DOWN | 0.65 | open |  |
| 11-11 00:33 | +15 | HYPE | DOWN | 0.65 | open |  |
| 11-11 00:33 | +10 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 00:33 | +5 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 00:33 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-11 00:33 | +20 | XRP | DOWN | 0.61 | 0.83 | 1.93 |
| 11-11 00:33 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-11 00:33 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-11 00:33 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 11-11 00:32 | +10 stop | ETH | UP | 0.64 | 0.83 | 1.63 |
| 11-11 00:32 | +5 | ETH | UP | 0.62 | 0.70 | 0.48 |
| 11-11 00:32 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 11-11 00:32 | +10 stop | DOGE | UP | 0.63 | 0.81 | 1.52 |
| 11-11 00:32 | +10 stop | SOL | DOWN | 0.59 | 0.41 | -2.14 |
| 11-11 00:32 | +20 | SOL | DOWN | 0.59 | open |  |
| 11-11 00:32 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-11 00:32 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-11 00:32 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-11 00:32 | +10 stop | ZEC | DOWN | 0.62 | 0.45 | -2.05 |
| 11-11 00:32 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-11 00:32 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-11 00:32 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-11 00:32 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-11 00:32 | +5 | DOGE | UP | 0.67 | 0.81 | 1.13 |
| 11-11 00:32 | +10 stop | NEAR | UP | 0.63 | 0.79 | 1.31 |
| 11-11 00:32 | +20 | NEAR | UP | 0.63 | 0.83 | 1.73 |
| 11-11 00:32 | +15 | NEAR | UP | 0.63 | 0.79 | 1.31 |
| 11-11 00:32 | +10 | NEAR | UP | 0.63 | 0.79 | 1.31 |
