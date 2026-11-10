# Range-Scalp Bot

*Updated Tue Nov 10 22:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54974 | 47947 | 7027 (94) | 6 | $-14994.63 | -4.3% |
| **+10¢** | 41079 | 32881 | 8198 (124) | 4 | $-13910.66 | -5.4% |
| **+15¢** | 34439 | 25605 | 8834 (158) | 3 | $-12633.01 | -5.8% |
| **+20¢** | 30656 | 21387 | 9269 (207) | 3 | $-11059.22 | -5.8% |
| **+10¢ (15¢ stop)** | 66984 | 66866 | 118 (73) | 0 | $-24764.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 22:21 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-10 22:19 | +15 | SOL | DOWN | 0.63 | 0.81 | 1.52 |
| 11-10 22:19 | +10 | ZEC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-10 22:19 | +15 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-10 22:18 | +10 stop | SOL | DOWN | 0.60 | 0.81 | 1.82 |
| 11-10 22:18 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 11-10 22:18 | +10 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 11-10 22:18 | +10 stop | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 11-10 22:18 | +5 | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 11-10 22:18 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-10 22:18 | +5 | ETH | DOWN | 0.62 | 0.71 | 0.58 |
| 11-10 22:18 | +10 stop | ZEC | DOWN | 0.62 | 0.87 | 2.25 |
| 11-10 22:18 | +10 stop | HYPE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-10 22:18 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-10 22:18 | +5 | BNB | UP | 0.38 | 0.64 | 2.26 |
| 11-10 22:18 | +5 | SOL | UP | 0.58 | open |  |
| 11-10 22:17 | +5 | XRP | UP | 0.61 | open |  |
| 11-10 22:17 | +10 stop | BTC | UP | 0.70 | 0.53 | -2.03 |
| 11-10 22:17 | +20 | BTC | UP | 0.70 | open |  |
| 11-10 22:17 | +15 | BTC | UP | 0.70 | open |  |
| 11-10 22:17 | +10 | BTC | UP | 0.70 | open |  |
| 11-10 22:17 | +5 | BTC | UP | 0.70 | open |  |
| 11-10 22:17 | +10 stop | HYPE | UP | 0.61 | 0.43 | -2.15 |
| 11-10 22:17 | +20 | HYPE | UP | 0.61 | open |  |
| 11-10 22:17 | +15 | HYPE | UP | 0.60 | open |  |
| 11-10 22:17 | +10 | HYPE | UP | 0.60 | open |  |
| 11-10 22:17 | +5 | HYPE | UP | 0.60 | open |  |
| 11-10 22:17 | +5 | ZEC | UP | 0.62 | open |  |
| 11-10 22:16 | +10 stop | SOL | UP | 0.60 | 0.35 | -2.83 |
| 11-10 22:16 | +10 | SOL | UP | 0.60 | open |  |
| 11-10 22:16 | +5 | SOL | UP | 0.60 | 0.66 | 0.27 |
| 11-10 22:16 | +5 | DOGE | UP | 0.60 | open |  |
| 11-10 22:16 | +10 stop | BNB | UP | 0.62 | 0.39 | -2.64 |
| 11-10 22:16 | +20 | BNB | UP | 0.62 | open |  |
| 11-10 22:16 | +15 | BNB | UP | 0.62 | open |  |
| 11-10 22:16 | +10 | BNB | UP | 0.62 | open |  |
| 11-10 22:16 | +5 | BNB | UP | 0.62 | 0.70 | 0.48 |
| 11-10 22:16 | +10 stop | SOL | DOWN | 0.49 | 0.61 | 0.85 |
| 11-10 22:16 | +20 | SOL | DOWN | 0.49 | 0.69 | 1.67 |
| 11-10 22:16 | +15 | SOL | DOWN | 0.49 | 0.64 | 1.15 |
