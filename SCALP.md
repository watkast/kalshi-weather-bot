# Range-Scalp Bot

*Updated Thu Nov 19 03:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64657 | 56414 | 8243 (124) | 3 | $-17501.28 | -4.3% |
| **+10¢** | 48301 | 38658 | 9643 (165) | 3 | $-16312.01 | -5.4% |
| **+15¢** | 40505 | 30107 | 10398 (210) | 3 | $-14737.93 | -5.8% |
| **+20¢** | 36072 | 25154 | 10918 (265) | 4 | $-13037.42 | -5.8% |
| **+10¢ (15¢ stop)** | 78670 | 78506 | 164 (98) | 0 | $-28909.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 03:06 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-19 03:05 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 11-19 03:05 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-19 03:05 | +10 stop | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 11-19 03:04 | +10 stop | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 11-19 03:04 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-19 03:04 | +10 stop | NEAR | DOWN | 0.60 | 0.74 | 1.09 |
| 11-19 03:04 | +10 stop | SOL | UP | 0.67 | 0.44 | -2.64 |
| 11-19 03:03 | +10 stop | DOGE | UP | 0.60 | 0.41 | -2.24 |
| 11-19 03:03 | +10 | HYPE | UP | 0.66 | open |  |
| 11-19 03:03 | +5 | HYPE | UP | 0.67 | open |  |
| 11-19 03:02 | +10 stop | DOGE | UP | 0.56 | 0.67 | 0.76 |
| 11-19 03:02 | +10 stop | SOL | UP | 0.57 | 0.69 | 0.87 |
| 11-19 03:02 | +10 stop | XRP | UP | 0.53 | 0.34 | -2.24 |
| 11-19 03:02 | +10 stop | ZEC | UP | 0.47 | 0.27 | -2.32 |
| 11-19 03:02 | +5 | ETH | UP | 0.68 | open |  |
| 11-19 03:02 | +10 stop | BNB | UP | 0.69 | 0.53 | -1.93 |
| 11-19 03:02 | +10 stop | BTC | UP | 0.70 | 0.45 | -2.83 |
| 11-19 03:02 | +20 | BTC | UP | 0.70 | open |  |
| 11-19 03:02 | +15 | BTC | UP | 0.70 | open |  |
| 11-19 03:02 | +10 | BTC | UP | 0.70 | open |  |
| 11-19 03:02 | +5 | BTC | UP | 0.70 | open |  |
| 11-19 03:01 | +10 stop | HYPE | UP | 0.61 | 0.33 | -3.13 |
| 11-19 03:01 | +20 | HYPE | UP | 0.62 | open |  |
| 11-19 03:01 | +15 | HYPE | UP | 0.60 | open |  |
| 11-19 03:01 | +10 | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-19 03:01 | +5 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 11-19 03:01 | +10 stop | ETH | UP | 0.62 | 0.46 | -1.95 |
| 11-19 03:01 | +20 | ETH | UP | 0.62 | open |  |
| 11-19 03:01 | +15 | ETH | UP | 0.62 | open |  |
| 11-19 03:01 | +10 | ETH | UP | 0.62 | open |  |
| 11-19 03:01 | +5 | ETH | UP | 0.60 | 0.66 | 0.27 |
| 11-19 03:01 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 11-19 03:01 | +20 | NEAR | DOWN | 0.62 | 0.84 | 1.93 |
| 11-19 03:01 | +15 | NEAR | DOWN | 0.61 | 0.78 | 1.40 |
| 11-19 03:01 | +10 | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-19 03:01 | +5 | NEAR | DOWN | 0.65 | 0.74 | 0.60 |
| 11-19 03:01 | +10 stop | DOGE | DOWN | 0.61 | 0.35 | -2.93 |
| 11-19 03:01 | +20 | DOGE | DOWN | 0.61 | 0.83 | 1.93 |
| 11-19 03:01 | +15 | DOGE | DOWN | 0.61 | 0.78 | 1.40 |
