# Range-Scalp Bot

*Updated Tue Nov 10 23:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55019 | 47981 | 7038 (94) | 3 | $-15046.32 | -4.3% |
| **+10¢** | 41112 | 32905 | 8207 (124) | 4 | $-13943.34 | -5.4% |
| **+15¢** | 34467 | 25624 | 8843 (158) | 6 | $-12661.61 | -5.9% |
| **+20¢** | 30682 | 21404 | 9278 (207) | 6 | $-11080.89 | -5.8% |
| **+10¢ (15¢ stop)** | 67029 | 66911 | 118 (73) | 4 | $-24772.50 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 23:04 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 11-10 23:04 | +20 | DOGE | DOWN | 0.66 | open |  |
| 11-10 23:04 | +15 | DOGE | DOWN | 0.66 | open |  |
| 11-10 23:04 | +10 | DOGE | DOWN | 0.66 | open |  |
| 11-10 23:04 | +5 | DOGE | DOWN | 0.66 | open |  |
| 11-10 23:04 | +5 | NEAR | UP | 0.66 | open |  |
| 11-10 23:03 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-10 23:03 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-10 23:03 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-10 23:03 | +10 | ZEC | DOWN | 0.59 | open |  |
| 11-10 23:03 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-10 23:03 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 11-10 23:03 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-10 23:03 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-10 23:03 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-10 23:03 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 23:03 | +5 | ETH | DOWN | 0.69 | 0.80 | 0.86 |
| 11-10 23:02 | +10 stop | HYPE | UP | 0.51 | open |  |
| 11-10 23:02 | +20 | HYPE | UP | 0.51 | open |  |
| 11-10 23:02 | +15 | HYPE | UP | 0.51 | open |  |
| 11-10 23:02 | +10 | HYPE | UP | 0.51 | open |  |
| 11-10 23:02 | +5 | HYPE | UP | 0.51 | 0.60 | 0.55 |
| 11-10 23:02 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-10 23:02 | +20 | NEAR | UP | 0.58 | open |  |
| 11-10 23:02 | +15 | NEAR | UP | 0.58 | open |  |
| 11-10 23:02 | +10 | NEAR | UP | 0.58 | open |  |
| 11-10 23:02 | +5 | NEAR | UP | 0.58 | 0.64 | 0.25 |
| 11-10 23:02 | +10 stop | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 11-10 23:02 | +20 | ETH | DOWN | 0.57 | 0.80 | 2.00 |
| 11-10 23:02 | +15 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 11-10 23:02 | +10 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 11-10 23:02 | +5 | ETH | DOWN | 0.57 | 0.66 | 0.56 |
| 11-10 23:02 | +10 stop | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-10 23:02 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-10 23:02 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-10 23:02 | +10 | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-10 23:02 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-10 23:01 | +10 stop | SOL | DOWN | 0.50 | 0.71 | 1.77 |
| 11-10 23:01 | +20 | SOL | DOWN | 0.50 | 0.71 | 1.77 |
| 11-10 23:01 | +15 | SOL | DOWN | 0.50 | 0.71 | 1.77 |
