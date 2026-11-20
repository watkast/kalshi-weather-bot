# Range-Scalp Bot

*Updated Fri Nov 20 01:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65626 | 57286 | 8340 (124) | 7 | $-17572.64 | -4.3% |
| **+10¢** | 49014 | 39261 | 9753 (165) | 7 | $-16344.92 | -5.3% |
| **+15¢** | 41103 | 30581 | 10522 (211) | 7 | $-14725.77 | -5.7% |
| **+20¢** | 36595 | 25542 | 11053 (266) | 7 | $-13036.60 | -5.7% |
| **+10¢ (15¢ stop)** | 79896 | 79732 | 164 (98) | 0 | $-29415.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 01:37 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-20 01:36 | +10 stop | BTC | DOWN | 0.62 | 0.85 | 2.04 |
| 11-20 01:36 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-20 01:34 | +5 | ETH | UP | 0.58 | open |  |
| 11-20 01:34 | +5 | BNB | UP | 0.59 | open |  |
| 11-20 01:34 | +5 | XRP | UP | 0.63 | open |  |
| 11-20 01:34 | +5 | ZEC | UP | 0.58 | open |  |
| 11-20 01:34 | +10 stop | DOGE | UP | 0.52 | 0.32 | -2.34 |
| 11-20 01:34 | +10 stop | SOL | UP | 0.54 | 0.39 | -1.85 |
| 11-20 01:33 | +10 stop | HYPE | DOWN | 0.60 | 0.76 | 1.30 |
| 11-20 01:33 | +10 stop | XRP | UP | 0.63 | 0.35 | -3.13 |
| 11-20 01:33 | +20 | XRP | UP | 0.63 | open |  |
| 11-20 01:33 | +15 | XRP | UP | 0.63 | open |  |
| 11-20 01:33 | +10 | XRP | UP | 0.63 | open |  |
| 11-20 01:33 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 11-20 01:33 | +10 stop | ZEC | UP | 0.59 | 0.26 | -3.61 |
| 11-20 01:33 | +20 | ZEC | UP | 0.59 | open |  |
| 11-20 01:33 | +15 | ZEC | UP | 0.59 | open |  |
| 11-20 01:33 | +10 | ZEC | UP | 0.59 | open |  |
| 11-20 01:33 | +5 | ZEC | UP | 0.59 | 0.68 | 0.57 |
| 11-20 01:33 | +5 | ETH | UP | 0.58 | 0.64 | 0.25 |
| 11-20 01:33 | +5 | BNB | UP | 0.60 | 0.66 | 0.27 |
| 11-20 01:32 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
| 11-20 01:32 | +20 | ETH | UP | 0.63 | open |  |
| 11-20 01:32 | +5 | ETH | UP | 0.62 | 0.67 | 0.17 |
| 11-20 01:32 | +10 stop | BNB | UP | 0.63 | 0.40 | -2.64 |
| 11-20 01:32 | +20 | BNB | UP | 0.63 | open |  |
| 11-20 01:32 | +15 | BNB | UP | 0.63 | open |  |
| 11-20 01:32 | +10 | BNB | UP | 0.63 | open |  |
| 11-20 01:32 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 11-20 01:32 | +10 stop | DOGE | UP | 0.66 | 0.48 | -2.14 |
| 11-20 01:32 | +20 | DOGE | UP | 0.66 | no | -6.76 |
| 11-20 01:32 | +15 | DOGE | UP | 0.66 | no | -6.76 |
| 11-20 01:32 | +10 | DOGE | UP | 0.66 | no | -6.76 |
| 11-20 01:32 | +5 | DOGE | UP | 0.66 | no | -6.76 |
| 11-20 01:32 | +10 stop | SOL | UP | 0.62 | 0.46 | -1.95 |
| 11-20 01:32 | +20 | SOL | UP | 0.62 | open |  |
| 11-20 01:32 | +15 | SOL | UP | 0.63 | open |  |
| 11-20 01:32 | +10 | SOL | UP | 0.62 | open |  |
| 11-20 01:32 | +5 | SOL | UP | 0.62 | open |  |
