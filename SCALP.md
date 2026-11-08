# Range-Scalp Bot

*Updated Sun Nov 08 01:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51757 | 45132 | 6625 (80) | 5 | $-14332.28 | -4.4% |
| **+10¢** | 38630 | 30906 | 7724 (106) | 5 | $-13323.78 | -5.5% |
| **+15¢** | 32348 | 24024 | 8324 (135) | 6 | $-12209.65 | -6.0% |
| **+20¢** | 28775 | 20048 | 8727 (180) | 7 | $-10752.15 | -6.0% |
| **+10¢ (15¢ stop)** | 63031 | 62928 | 103 (61) | 2 | $-23338.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 01:02 | +10 stop | BTC | UP | 0.63 | open |  |
| 11-08 01:02 | +10 stop | SOL | UP | 0.55 | 0.65 | 0.66 |
| 11-08 01:02 | +10 stop | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 11-08 01:02 | +20 | DOGE | UP | 0.70 | open |  |
| 11-08 01:02 | +15 | DOGE | UP | 0.70 | open |  |
| 11-08 01:02 | +10 | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 11-08 01:02 | +5 | DOGE | UP | 0.70 | 0.80 | 0.73 |
| 11-08 01:02 | +10 stop | XRP | DOWN | 0.56 | open |  |
| 11-08 01:02 | +20 | XRP | DOWN | 0.56 | open |  |
| 11-08 01:02 | +15 | XRP | DOWN | 0.56 | open |  |
| 11-08 01:02 | +10 | XRP | DOWN | 0.56 | open |  |
| 11-08 01:02 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-08 01:01 | +10 stop | ETH | UP | 0.53 | 0.65 | 0.86 |
| 11-08 01:01 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-08 01:01 | +10 stop | NEAR | UP | 0.60 | 0.74 | 1.09 |
| 11-08 01:01 | +20 | NEAR | UP | 0.60 | open |  |
| 11-08 01:01 | +15 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 11-08 01:01 | +10 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-08 01:01 | +5 | NEAR | UP | 0.60 | 0.69 | 0.59 |
| 11-08 01:01 | +10 stop | BTC | UP | 0.70 | 0.49 | -2.43 |
| 11-08 01:01 | +10 stop | BTC | DOWN | 0.54 | 0.39 | -1.85 |
| 11-08 01:01 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-08 01:01 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-08 01:01 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-08 01:01 | +5 | BTC | DOWN | 0.55 | open |  |
| 11-08 01:00 | +10 stop | ETH | DOWN | 0.61 | 0.39 | -2.54 |
| 11-08 01:00 | +20 | ETH | DOWN | 0.61 | open |  |
| 11-08 01:00 | +15 | ETH | DOWN | 0.61 | open |  |
| 11-08 01:00 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-08 01:00 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-08 01:00 | +10 stop | SOL | DOWN | 0.59 | 0.42 | -2.07 |
| 11-08 01:00 | +20 | SOL | DOWN | 0.59 | open |  |
| 11-08 01:00 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-08 01:00 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-08 01:00 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-08 01:00 | +10 stop | HYPE | DOWN | 0.59 | 0.34 | -2.88 |
| 11-08 01:00 | +20 | HYPE | DOWN | 0.59 | open |  |
| 11-08 01:00 | +15 | HYPE | DOWN | 0.59 | open |  |
| 11-08 01:00 | +10 | HYPE | DOWN | 0.59 | open |  |
| 11-08 01:00 | +5 | HYPE | DOWN | 0.59 | open |  |
