# Range-Scalp Bot

*Updated Thu Nov 19 02:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64630 | 56387 | 8243 (124) | 4 | $-17521.39 | -4.3% |
| **+10¢** | 48281 | 38638 | 9643 (165) | 5 | $-16335.41 | -5.4% |
| **+15¢** | 40485 | 30088 | 10397 (210) | 7 | $-14761.91 | -5.8% |
| **+20¢** | 36055 | 25138 | 10917 (265) | 7 | $-13063.33 | -5.8% |
| **+10¢ (15¢ stop)** | 78627 | 78463 | 164 (98) | 5 | $-28870.55 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 02:47 | +10 stop | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 11-19 02:47 | +20 | NEAR | UP | 0.53 | open |  |
| 11-19 02:47 | +15 | NEAR | UP | 0.53 | open |  |
| 11-19 02:47 | +10 | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 11-19 02:47 | +5 | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 11-19 02:47 | +10 stop | ETH | UP | 0.50 | open |  |
| 11-19 02:47 | +20 | ETH | UP | 0.50 | open |  |
| 11-19 02:47 | +15 | ETH | UP | 0.50 | open |  |
| 11-19 02:47 | +10 | ETH | UP | 0.50 | open |  |
| 11-19 02:47 | +5 | ETH | UP | 0.50 | 0.55 | 0.14 |
| 11-19 02:47 | +10 stop | XRP | UP | 0.48 | open |  |
| 11-19 02:47 | +20 | XRP | UP | 0.49 | open |  |
| 11-19 02:47 | +15 | XRP | UP | 0.49 | open |  |
| 11-19 02:47 | +10 | XRP | UP | 0.49 | open |  |
| 11-19 02:47 | +5 | XRP | UP | 0.49 | open |  |
| 11-19 02:46 | +5 | DOGE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-19 02:46 | +10 stop | ZEC | UP | 0.66 | open |  |
| 11-19 02:46 | +20 | ZEC | UP | 0.66 | open |  |
| 11-19 02:46 | +15 | ZEC | UP | 0.67 | open |  |
| 11-19 02:46 | +10 | ZEC | UP | 0.68 | open |  |
| 11-19 02:46 | +5 | ZEC | UP | 0.68 | open |  |
| 11-19 02:46 | +10 stop | BTC | UP | 0.65 | open |  |
| 11-19 02:46 | +20 | BTC | UP | 0.65 | open |  |
| 11-19 02:46 | +15 | BTC | UP | 0.66 | open |  |
| 11-19 02:46 | +10 | BTC | UP | 0.66 | open |  |
| 11-19 02:46 | +5 | BTC | UP | 0.66 | open |  |
| 11-19 02:45 | +10 stop | DOGE | DOWN | 0.52 | 0.63 | 0.75 |
| 11-19 02:45 | +20 | DOGE | DOWN | 0.52 | open |  |
| 11-19 02:45 | +15 | DOGE | DOWN | 0.52 | open |  |
| 11-19 02:45 | +10 | DOGE | DOWN | 0.52 | 0.63 | 0.75 |
| 11-19 02:45 | +5 | DOGE | DOWN | 0.52 | 0.57 | 0.14 |
| 11-19 02:45 | +10 stop | HYPE | DOWN | 0.53 | open |  |
| 11-19 02:45 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-19 02:45 | +15 | HYPE | DOWN | 0.53 | open |  |
| 11-19 02:45 | +10 | HYPE | DOWN | 0.53 | open |  |
| 11-19 02:45 | +5 | HYPE | DOWN | 0.54 | open |  |
| 11-19 02:43 | +10 stop | XRP | DOWN | 0.63 | 0.84 | 1.85 |
| 11-19 02:43 | +15 | XRP | DOWN | 0.59 | 0.84 | 2.23 |
| 11-19 02:43 | +10 | XRP | DOWN | 0.58 | 0.84 | 2.29 |
| 11-19 02:43 | +5 | XRP | DOWN | 0.58 | 0.84 | 2.29 |
