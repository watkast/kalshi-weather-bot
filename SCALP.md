# Range-Scalp Bot

*Updated Mon Oct 19 21:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24596 | 21412 | 3184 (31) | 6 | $-7184.24 | -4.6% |
| **+10¢** | 18490 | 14811 | 3679 (46) | 8 | $-6405.34 | -5.5% |
| **+15¢** | 15481 | 11520 | 3961 (70) | 8 | $-5756.52 | -5.9% |
| **+20¢** | 13693 | 9545 | 4148 (88) | 8 | $-5171.95 | -6.0% |
| **+10¢ (15¢ stop)** | 30236 | 30184 | 52 (30) | 3 | $-11394.35 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 21:25 | +10 stop | ETH | DOWN | 0.52 | open |  |
| 10-19 21:25 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-19 21:23 | +10 stop | SOL | UP | 0.71 | open |  |
| 10-19 21:23 | +15 | SOL | UP | 0.71 | open |  |
| 10-19 21:23 | +10 | SOL | UP | 0.71 | open |  |
| 10-19 21:23 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 10-19 21:23 | +10 stop | DOGE | UP | 0.57 | 0.68 | 0.76 |
| 10-19 21:23 | +10 stop | ETH | UP | 0.60 | 0.43 | -2.05 |
| 10-19 21:23 | +10 stop | BNB | UP | 0.61 | open |  |
| 10-19 21:22 | +10 stop | HYPE | UP | 0.66 | 0.83 | 1.43 |
| 10-19 21:22 | +5 | HYPE | UP | 0.66 | 0.83 | 1.44 |
| 10-19 21:22 | +10 stop | HYPE | UP | 0.54 | 0.67 | 0.96 |
| 10-19 21:22 | +5 | HYPE | UP | 0.53 | 0.67 | 1.06 |
| 10-19 21:22 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-19 21:21 | +10 stop | ETH | DOWN | 0.59 | 0.44 | -1.85 |
| 10-19 21:21 | +10 | ETH | DOWN | 0.59 | open |  |
| 10-19 21:21 | +5 | ETH | DOWN | 0.59 | open |  |
| 10-19 21:21 | +10 stop | DOGE | DOWN | 0.64 | 0.47 | -2.05 |
| 10-19 21:21 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-19 21:21 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-19 21:21 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-19 21:21 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-19 21:21 | +10 stop | BNB | DOWN | 0.60 | 0.40 | -2.34 |
| 10-19 21:21 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-19 21:21 | +15 | BNB | DOWN | 0.60 | open |  |
| 10-19 21:21 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-19 21:21 | +5 | BNB | DOWN | 0.60 | open |  |
| 10-19 21:20 | +10 stop | HYPE | DOWN | 0.49 | 0.25 | -2.72 |
| 10-19 21:20 | +5 | HYPE | DOWN | 0.51 | 0.57 | 0.24 |
| 10-19 21:20 | +10 stop | ZEC | UP | 0.66 | 0.80 | 1.12 |
| 10-19 21:18 | +10 stop | ZEC | DOWN | 0.62 | 0.46 | -1.95 |
| 10-19 21:18 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-19 21:18 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-19 21:18 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-19 21:18 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 10-19 21:17 | +10 stop | XRP | DOWN | 0.64 | 0.44 | -2.35 |
| 10-19 21:17 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-19 21:17 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-19 21:17 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-19 21:17 | +5 | XRP | DOWN | 0.64 | open |  |
