# Range-Scalp Bot

*Updated Sun Nov 15 15:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60947 | 53175 | 7772 (112) | 4 | $-16477.48 | -4.3% |
| **+10¢** | 45528 | 36422 | 9106 (150) | 4 | $-15491.14 | -5.4% |
| **+15¢** | 38127 | 28306 | 9821 (188) | 5 | $-14158.97 | -5.9% |
| **+20¢** | 33982 | 23681 | 10301 (240) | 5 | $-12431.93 | -5.8% |
| **+10¢ (15¢ stop)** | 74177 | 74026 | 151 (89) | 2 | $-27298.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 15:13 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 11-15 15:13 | +10 stop | NEAR | DOWN | 0.63 | open |  |
| 11-15 15:12 | +10 stop | XRP | UP | 0.41 | 0.58 | 1.33 |
| 11-15 15:11 | +10 stop | ZEC | UP | 0.64 | 0.22 | -4.50 |
| 11-15 15:11 | +20 | ZEC | UP | 0.64 | open |  |
| 11-15 15:11 | +15 | ZEC | UP | 0.63 | open |  |
| 11-15 15:11 | +10 | ZEC | UP | 0.63 | open |  |
| 11-15 15:11 | +5 | ZEC | UP | 0.63 | open |  |
| 11-15 15:11 | +10 stop | ETH | UP | 0.55 | 0.19 | -3.89 |
| 11-15 15:11 | +20 | ETH | UP | 0.55 | open |  |
| 11-15 15:11 | +15 | ETH | UP | 0.55 | open |  |
| 11-15 15:11 | +10 | ETH | UP | 0.55 | open |  |
| 11-15 15:11 | +5 | ETH | UP | 0.55 | open |  |
| 11-15 15:10 | +10 | XRP | UP | 0.64 | open |  |
| 11-15 15:10 | +5 | XRP | UP | 0.65 | open |  |
| 11-15 15:10 | +10 stop | XRP | UP | 0.71 | 0.51 | -2.33 |
| 11-15 15:10 | +20 | XRP | UP | 0.71 | open |  |
| 11-15 15:10 | +15 | XRP | UP | 0.71 | open |  |
| 11-15 15:10 | +10 stop | HYPE | UP | 0.53 | 0.67 | 1.06 |
| 11-15 15:10 | +20 | HYPE | UP | 0.53 | open |  |
| 11-15 15:10 | +15 | HYPE | UP | 0.53 | open |  |
| 11-15 15:10 | +10 | HYPE | UP | 0.53 | 0.67 | 1.06 |
| 11-15 15:10 | +5 | HYPE | UP | 0.53 | 0.67 | 1.06 |
| 11-15 15:08 | +10 stop | NEAR | DOWN | 0.71 | 0.18 | -5.54 |
| 11-15 15:08 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-15 15:08 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-15 15:08 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-15 15:08 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-15 15:04 | +10 stop | ZEC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-15 15:04 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 11-15 15:03 | +20 | ZEC | UP | 0.52 | 0.81 | 2.61 |
| 11-15 15:03 | +15 | ZEC | UP | 0.52 | 0.81 | 2.61 |
| 11-15 15:03 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-15 15:02 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-15 15:02 | +10 | ZEC | UP | 0.63 | 0.81 | 1.52 |
| 11-15 15:02 | +5 | ZEC | UP | 0.63 | 0.81 | 1.52 |
| 11-15 15:02 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.73 |
| 11-15 15:02 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.77 |
| 11-15 15:02 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.27 |
| 11-15 15:02 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
