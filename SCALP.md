# Range-Scalp Bot

*Updated Tue Nov 17 18:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63123 | 55067 | 8056 (117) | 7 | $-17149.39 | -4.3% |
| **+10¢** | 47159 | 37735 | 9424 (159) | 7 | $-15994.71 | -5.4% |
| **+15¢** | 39531 | 29369 | 10162 (201) | 8 | $-14496.39 | -5.8% |
| **+20¢** | 35221 | 24557 | 10664 (256) | 8 | $-12735.13 | -5.8% |
| **+10¢ (15¢ stop)** | 76826 | 76670 | 156 (92) | 0 | $-28283.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 18:09 | +10 stop | BNB | UP | 0.45 | 0.57 | 0.86 |
| 11-17 18:09 | +10 stop | ETH | UP | 0.49 | 0.62 | 0.95 |
| 11-17 18:09 | +10 stop | DOGE | UP | 0.50 | 0.62 | 0.85 |
| 11-17 18:08 | +10 stop | XRP | DOWN | 0.55 | 0.71 | 1.27 |
| 11-17 18:08 | +10 stop | HYPE | UP | 0.68 | 0.40 | -3.13 |
| 11-17 18:08 | +20 | HYPE | UP | 0.68 | open |  |
| 11-17 18:08 | +15 | HYPE | UP | 0.68 | open |  |
| 11-17 18:08 | +10 | HYPE | UP | 0.68 | open |  |
| 11-17 18:08 | +5 | HYPE | UP | 0.67 | open |  |
| 11-17 18:08 | +10 stop | NEAR | DOWN | 0.49 | 0.64 | 1.15 |
| 11-17 18:08 | +10 stop | BNB | UP | 0.57 | 0.68 | 0.76 |
| 11-17 18:08 | +10 stop | ETH | UP | 0.57 | 0.69 | 0.87 |
| 11-17 18:08 | +10 stop | BTC | UP | 0.44 | 0.64 | 1.65 |
| 11-17 18:07 | +10 stop | XRP | UP | 0.54 | 0.33 | -2.44 |
| 11-17 18:07 | +10 stop | NEAR | UP | 0.67 | 0.49 | -2.14 |
| 11-17 18:06 | +10 stop | NEAR | DOWN | 0.43 | 0.54 | 0.70 |
| 11-17 18:05 | +10 stop | BNB | UP | 0.55 | 0.74 | 1.58 |
| 11-17 18:05 | +15 | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 11-17 18:05 | +5 | HYPE | UP | 0.60 | 0.68 | 0.47 |
| 11-17 18:05 | +10 stop | ETH | UP | 0.62 | 0.74 | 0.89 |
| 11-17 18:05 | +10 stop | DOGE | UP | 0.61 | 0.77 | 1.30 |
| 11-17 18:05 | +10 stop | SOL | UP | 0.60 | 0.70 | 0.69 |
| 11-17 18:05 | +10 stop | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 11-17 18:04 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 11-17 18:04 | +10 | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 11-17 18:04 | +5 | HYPE | UP | 0.58 | 0.67 | 0.56 |
| 11-17 18:03 | +10 stop | NEAR | DOWN | 0.69 | 0.49 | -2.33 |
| 11-17 18:03 | +10 stop | HYPE | UP | 0.50 | 0.62 | 0.85 |
| 11-17 18:03 | +10 | HYPE | UP | 0.50 | 0.62 | 0.85 |
| 11-17 18:02 | +5 | HYPE | UP | 0.57 | 0.62 | 0.15 |
| 11-17 18:01 | +10 stop | BNB | DOWN | 0.57 | 0.38 | -2.25 |
| 11-17 18:01 | +20 | BNB | DOWN | 0.57 | open |  |
| 11-17 18:01 | +15 | BNB | DOWN | 0.57 | open |  |
| 11-17 18:01 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-17 18:01 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-17 18:01 | +10 stop | ETH | DOWN | 0.58 | 0.43 | -1.86 |
| 11-17 18:01 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-17 18:01 | +15 | ETH | DOWN | 0.59 | open |  |
| 11-17 18:01 | +10 | ETH | DOWN | 0.59 | open |  |
| 11-17 18:01 | +5 | ETH | DOWN | 0.59 | open |  |
