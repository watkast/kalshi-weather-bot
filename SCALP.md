# Range-Scalp Bot

*Updated Sun Nov 22 13:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68771 | 60012 | 8759 (142) | 4 | $-18487.32 | -4.3% |
| **+10¢** | 51325 | 41094 | 10231 (186) | 4 | $-17146.01 | -5.3% |
| **+15¢** | 43013 | 31983 | 11030 (237) | 5 | $-15401.51 | -5.7% |
| **+20¢** | 38291 | 26702 | 11589 (295) | 6 | $-13719.30 | -5.7% |
| **+10¢ (15¢ stop)** | 83747 | 83562 | 185 (116) | 0 | $-30842.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 13:55 | +10 stop | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 11-22 13:55 | +20 | DOGE | DOWN | 0.42 | open |  |
| 11-22 13:55 | +15 | DOGE | DOWN | 0.40 | 0.61 | 1.76 |
| 11-22 13:55 | +10 | DOGE | DOWN | 0.40 | 0.61 | 1.76 |
| 11-22 13:55 | +5 | DOGE | DOWN | 0.43 | 0.61 | 1.48 |
| 11-22 13:55 | +10 stop | ETH | DOWN | 0.31 | 0.58 | 2.37 |
| 11-22 13:55 | +20 | ETH | DOWN | 0.31 | 0.58 | 2.37 |
| 11-22 13:55 | +15 | ETH | DOWN | 0.32 | 0.58 | 2.26 |
| 11-22 13:55 | +10 | ETH | DOWN | 0.29 | 0.58 | 2.57 |
| 11-22 13:55 | +5 | ETH | DOWN | 0.30 | 0.58 | 2.47 |
| 11-22 13:55 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-22 13:55 | +10 stop | NEAR | UP | 0.69 | 0.90 | 1.89 |
| 11-22 13:55 | +10 | NEAR | UP | 0.68 | 0.90 | 1.98 |
| 11-22 13:55 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 11-22 13:54 | +10 stop | HYPE | DOWN | 0.51 | 0.34 | -2.04 |
| 11-22 13:54 | +15 | HYPE | DOWN | 0.51 | open |  |
| 11-22 13:54 | +10 | HYPE | DOWN | 0.51 | open |  |
| 11-22 13:54 | +5 | HYPE | DOWN | 0.51 | open |  |
| 11-22 13:54 | +10 stop | NEAR | DOWN | 0.53 | 0.33 | -2.30 |
| 11-22 13:54 | +20 | NEAR | DOWN | 0.52 | open |  |
| 11-22 13:54 | +15 | NEAR | DOWN | 0.52 | open |  |
| 11-22 13:54 | +10 | NEAR | DOWN | 0.52 | 0.62 | 0.65 |
| 11-22 13:54 | +5 | NEAR | DOWN | 0.52 | 0.62 | 0.65 |
| 11-22 13:54 | +10 stop | BTC | DOWN | 0.55 | 0.28 | -3.03 |
| 11-22 13:54 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-22 13:54 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-22 13:54 | +5 | BTC | DOWN | 0.55 | open |  |
| 11-22 13:54 | +10 stop | SOL | DOWN | 0.55 | 0.36 | -2.25 |
| 11-22 13:54 | +10 stop | ZEC | DOWN | 0.48 | 0.27 | -2.42 |
| 11-22 13:53 | +5 | BTC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-22 13:53 | +10 stop | ZEC | UP | 0.55 | 0.37 | -2.15 |
| 11-22 13:52 | +10 stop | SOL | UP | 0.56 | 0.37 | -2.25 |
| 11-22 13:52 | +10 stop | BTC | DOWN | 0.54 | 0.72 | 1.47 |
| 11-22 13:52 | +20 | BTC | DOWN | 0.54 | open |  |
| 11-22 13:52 | +15 | BTC | DOWN | 0.54 | 0.72 | 1.47 |
| 11-22 13:52 | +10 | BTC | DOWN | 0.54 | 0.72 | 1.47 |
| 11-22 13:52 | +5 | BTC | DOWN | 0.54 | 0.62 | 0.45 |
| 11-22 13:52 | +10 stop | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 11-22 13:51 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-22 13:51 | +10 stop | SOL | DOWN | 0.59 | 0.42 | -2.05 |
